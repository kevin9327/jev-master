"""Confidence-gated routing: the answer is what; confidence is whether to act.

Pattern: https://docs.typesafe.ai/patterns/confidence-routing
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jev_master.answers import ChoiceAnswer, NoulAnswer, ScoreAnswer, answers_as_json
from jev_master.client import Transport, choice_question, evaluate, noul_question, score_question
from jev_master.key import load_api_key

SAMPLE_STATE = (
    "Voice transcript: yeah go ahead and send the pending transfer, "
    "I already checked the amount."
)


def gate_questions() -> dict[str, dict[str, Any]]:
    return {
        "intent": choice_question(
            "What action is the user requesting?",
            {
                "check_balance": "Check the balance of an account",
                "approve_transfer": "Approve the pending transfer request",
                "other": "Something else",
            },
        ),
        "stakes": score_question(
            "How irreversible is the requested action if it is wrong?",
            [
                "Read-only, easy to undo",
                "Reversible with effort",
                "Money moves and is hard to unwind",
            ],
        ),
        "is_explicit": noul_question(
            "The user explicitly confirmed the action in this utterance",
            {"true": "Clear confirmation", "false": "Ambiguous or off-topic"},
        ),
    }


def compose_confidence_gate(answers: dict[str, Any]) -> dict[str, Any]:
    intent = answers["intent"]
    stakes = answers["stakes"]
    is_explicit = answers["is_explicit"]
    if not isinstance(intent, ChoiceAnswer):
        raise TypeError("intent must be a ChoiceAnswer")
    if not isinstance(stakes, ScoreAnswer):
        raise TypeError("stakes must be a ScoreAnswer")
    if not isinstance(is_explicit, NoulAnswer):
        raise TypeError("is_explicit must be a NoulAnswer")

    if intent.confidence < 0.6:
        decision = "escalate"
        reason = "low_confidence"
    elif intent.choice == "check_balance":
        decision = "act"
        reason = "low_stakes_read"
    elif intent.choice == "approve_transfer":
        if intent.confidence > 0.85 and is_explicit.noul >= 0.8 and stakes.score >= 1.5:
            decision = "act"
            reason = "high_confidence_confirmed"
        elif intent.confidence >= 0.6:
            decision = "confirm"
            reason = "high_stakes_need_verify"
        else:
            decision = "escalate"
            reason = "transfer_uncertain"
    else:
        decision = "escalate"
        reason = "unhandled_intent"

    return {
        "intent": intent.choice,
        "action": decision,
        "reason": reason,
        "confidence": intent.confidence,
        "stakes": stakes.score,
        "explicit": is_explicit.noul,
    }


def run_gate(
    state: str,
    *,
    api_key: str = "test-key",
    transport: Transport | None = None,
) -> dict[str, Any]:
    result = evaluate(state, gate_questions(), api_key=api_key, transport=transport)
    decision = compose_confidence_gate(result.answers)
    return {
        "app": "confidence_gate",
        "pattern": "confidence-gated-routing",
        "model": result.model,
        "state": state,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Confidence-gate a voice banking command")
    parser.add_argument("--state", help="Path to a state file")
    parser.add_argument("--text", help="Inline state text")
    args = parser.parse_args(argv)
    state = args.text if args.text else (
        Path(args.state).read_text(encoding="utf-8").strip() if args.state else SAMPLE_STATE
    )
    json.dump(run_gate(state, api_key=load_api_key()), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

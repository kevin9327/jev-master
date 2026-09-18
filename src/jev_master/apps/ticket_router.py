"""Intent routing: mix Choice + Score + Noul, then route in code.

Pattern: https://docs.typesafe.ai/patterns/intent-routing
Questions match the TypeSafe ticket sample (department / frustration / is_urgent).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jev_master.answers import ChoiceAnswer, NoulAnswer, ScoreAnswer, answers_as_json
from jev_master.client import (
    Transport,
    choice_question,
    evaluate,
    noul_question,
    score_question,
)
from jev_master.key import load_api_key

SAMPLE_STATE = (
    "Hi, I've been trying to connect my Stripe account for 3 days and it keeps "
    "failing. I'm losing sales. Please help ASAP."
)


def mixed_ticket_questions() -> dict[str, dict[str, Any]]:
    """One request with all three primitives, keyed like the docs sample."""
    return {
        "department": choice_question(
            "Which team should handle this",
            {
                "billing": "Payment or subscription issues",
                "technical": "Bugs or integration problems",
                "sales": "Pricing or account questions",
            },
        ),
        "frustration": score_question(
            "How frustrated the customer appears",
            [
                "Calm, just stating facts",
                "Frustrated but civil",
                "Very angry, strong language",
            ],
        ),
        "is_urgent": noul_question(
            "The message conveys urgency or time-sensitivity",
            {
                "true": "Explicitly time-sensitive",
                "false": "No urgency expressed",
            },
        ),
    }


def compose_ticket_route(answers: dict[str, Any]) -> dict[str, Any]:
    """Code owns control flow: department + escalate-or-act."""
    department = answers["department"]
    frustration = answers["frustration"]
    is_urgent = answers["is_urgent"]
    if not isinstance(department, ChoiceAnswer):
        raise TypeError("department must be a ChoiceAnswer")
    if not isinstance(frustration, ScoreAnswer):
        raise TypeError("frustration must be a ScoreAnswer")
    if not isinstance(is_urgent, NoulAnswer):
        raise TypeError("is_urgent must be a NoulAnswer")

    if department.confidence < 0.5:
        action = "escalate"
        handler = "human_triage"
    elif is_urgent.noul >= 0.85 and frustration.score >= 1.5:
        action = "escalate"
        handler = "priority_human"
    elif is_urgent.noul >= 0.7:
        action = "act"
        handler = f"{department.choice}_priority_queue"
    else:
        action = "act"
        handler = f"{department.choice}_queue"

    return {
        "department": department.choice,
        "action": action,
        "handler": handler,
        "urgency": is_urgent.noul,
        "frustration": frustration.score,
        "confidence": department.confidence,
    }


def run_ticket(
    state: str,
    *,
    api_key: str = "test-key",
    transport: Transport | None = None,
) -> dict[str, Any]:
    questions = mixed_ticket_questions()
    result = evaluate(state, questions, api_key=api_key, transport=transport)
    decision = compose_ticket_route(result.answers)
    return {
        "app": "ticket_router",
        "pattern": "intent-routing",
        "model": result.model,
        "state": state,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def _read_state(path: str | None) -> str:
    if not path:
        return SAMPLE_STATE
    return Path(path).read_text(encoding="utf-8").strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Route a support ticket with mixed Jev primitives")
    parser.add_argument("--state", help="Path to a text/JSON state file")
    parser.add_argument("--text", help="Inline state text")
    args = parser.parse_args(argv)
    state = args.text if args.text else _read_state(args.state)
    payload = run_ticket(state, api_key=load_api_key())
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

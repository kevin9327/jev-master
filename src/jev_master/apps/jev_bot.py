"""JevBot: support bot. Jev classifies; canned templates in code. Not a chatbot."""

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
    "Hi, I've been trying to connect my Stripe account for 3 days and it keeps "
    "failing. I'm losing sales. Please help ASAP."
)

TEMPLATES = {
    "billing_help": "We received a billing request. A specialist will check charges and subscriptions.",
    "tech_help": "We received an integration issue. Check API keys and webhook logs while we route this.",
    "account_help": "We received an account request. Identity checks stay in the account team queue.",
    "human_handoff": "This needs a human. You are in the priority queue.",
    "blocked": "This message was blocked by policy. A human will review if it was a mistake.",
    "off_topic": "This channel is for product support. Please restate the account or technical issue.",
}


def bot_questions() -> dict[str, dict[str, Any]]:
    return {
        "intent": choice_question(
            "What is the user's support intent?",
            {
                "billing": "Payment, invoice, or subscription",
                "technical": "Bug, outage, or integration failure",
                "account": "Login, permissions, or profile",
                "off_topic": "Not a product support request",
            },
        ),
        "severity": score_question(
            "How severe is the tone?",
            ["Calm", "Frustrated", "Abusive"],
        ),
        "needs_human": noul_question(
            "A human agent should take this conversation now",
        ),
    }


def compose_bot_action(answers: dict[str, Any]) -> dict[str, Any]:
    intent = answers["intent"]
    severity = answers["severity"]
    needs_human = answers["needs_human"]
    if not isinstance(intent, ChoiceAnswer):
        raise TypeError("intent must be a ChoiceAnswer")
    if not isinstance(severity, ScoreAnswer):
        raise TypeError("severity must be a ScoreAnswer")
    if not isinstance(needs_human, NoulAnswer):
        raise TypeError("needs_human must be a NoulAnswer")

    if severity.score >= 2.0 and needs_human.noul >= 0.7:
        action, template_id = "block", "blocked"
    elif intent.confidence < 0.5 or needs_human.noul >= 0.8 or severity.score >= 1.6:
        action, template_id = "escalate", "human_handoff"
    elif intent.choice == "billing":
        action, template_id = "reply", "billing_help"
    elif intent.choice == "technical":
        action, template_id = "reply", "tech_help"
    elif intent.choice == "account":
        action, template_id = "reply", "account_help"
    else:
        action, template_id = "reply", "off_topic"

    return {
        "intent": intent.choice,
        "action": action,
        "template_id": template_id,
        "reply": TEMPLATES[template_id],
        "confidence": intent.confidence,
        "severity": severity.score,
        "needs_human": needs_human.noul,
    }


def run_bot(state: str, *, api_key: str = "test-key", transport: Transport | None = None) -> dict[str, Any]:
    result = evaluate(state, bot_questions(), api_key=api_key, transport=transport)
    decision = compose_bot_action(result.answers)
    return {
        "app": "jev_bot",
        "pattern": "intent-routing",
        "model": result.model,
        "state": state,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="JevBot canned-reply support bot")
    parser.add_argument("--state", help="Path to a state file")
    parser.add_argument("--text", help="Inline state text")
    args = parser.parse_args(argv)
    state = args.text if args.text else (
        Path(args.state).read_text(encoding="utf-8").strip() if args.state else SAMPLE_STATE
    )
    json.dump(run_bot(state, api_key=load_api_key()), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

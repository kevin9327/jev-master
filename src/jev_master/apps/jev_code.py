"""JevCode: diff merge gate. merge / comment / block in code. Not a codegen."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jev_master.answers import ChoiceAnswer, NoulAnswer, ScoreAnswer, answers_as_json
from jev_master.client import Transport, choice_question, evaluate, noul_question, score_question
from jev_master.key import load_api_key

SAMPLE_STATE = """\
diff --git a/auth.py b/auth.py
@@ -10,7 +10,7 @@ def login(user, password):
-    query = "SELECT * FROM users WHERE name='" + user + "'"
+    query = "SELECT * FROM users WHERE name='" + user + "' OR 1=1"
     return db.execute(query)
"""


def code_questions() -> dict[str, dict[str, Any]]:
    return {
        "review": choice_question(
            "How should a reviewer treat this diff?",
            {
                "approve": "Safe to merge as written",
                "comment": "Needs discussion but not a hard block",
                "request_changes": "Must change before merge",
            },
        ),
        "risk": score_question(
            "How risky is this change if merged as-is?",
            [
                "Cosmetic or docs",
                "Local, contained logic",
                "Cross-cutting behavior",
                "Security-sensitive (auth, injection, secrets)",
            ],
        ),
        "tests_missing": noul_question(
            "This change needs tests that are not present in the diff",
        ),
    }


def compose_review_gate(answers: dict[str, Any]) -> dict[str, Any]:
    review = answers["review"]
    risk = answers["risk"]
    tests_missing = answers["tests_missing"]
    if not isinstance(review, ChoiceAnswer):
        raise TypeError("review must be a ChoiceAnswer")
    if not isinstance(risk, ScoreAnswer):
        raise TypeError("risk must be a ScoreAnswer")
    if not isinstance(tests_missing, NoulAnswer):
        raise TypeError("tests_missing must be a NoulAnswer")

    if review.confidence < 0.5 or review.choice == "request_changes" or risk.score >= 2.5 or tests_missing.noul >= 0.75:
        gate = "block"
    elif review.choice == "comment" or risk.score >= 1.2:
        gate = "comment"
    else:
        gate = "merge"

    return {
        "gate": gate,
        "review": review.choice,
        "risk": risk.score,
        "tests_missing": tests_missing.noul,
        "confidence": review.confidence,
    }


def run_code(state: str, *, api_key: str = "test-key", transport: Transport | None = None) -> dict[str, Any]:
    result = evaluate(state, code_questions(), api_key=api_key, transport=transport)
    decision = compose_review_gate(result.answers)
    return {
        "app": "jev_code",
        "pattern": "confidence-gated-routing",
        "model": result.model,
        "state": state,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="JevCode diff merge gate")
    parser.add_argument("--state", help="Path to a diff/patch file")
    parser.add_argument("--text", help="Inline diff text")
    args = parser.parse_args(argv)
    state = args.text if args.text else (
        Path(args.state).read_text(encoding="utf-8").strip() if args.state else SAMPLE_STATE
    )
    json.dump(run_code(state, api_key=load_api_key()), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

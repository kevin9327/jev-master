"""Shipped builders + composers for JevBot, JevHarness, JevCode."""

from __future__ import annotations

from jev_master.answers import parse_answer
from jev_master.apps.jev_bot import bot_questions, compose_bot_action, run_bot
from jev_master.apps.jev_code import code_questions, compose_review_gate, run_code
from jev_master.apps.jev_harness import compose_harness_gate, harness_questions, run_harness
from jev_master.client import build_systemone_payload


def _types(questions: dict) -> set[str]:
    return {item["type"] for item in questions.values()}


def test_new_app_payloads_mix_choice_score_noul() -> None:
    for questions in (bot_questions(), harness_questions(), code_questions()):
        payload = build_systemone_payload("state", questions)
        assert payload["model"] == "jev-latest"
        assert _types(payload["questions"]) == {"choice", "score", "noul"}


def test_bot_composer_escalates_low_confidence() -> None:
    answers = {
        "intent": parse_answer(
            {
                "type": "choice",
                "choice": "billing",
                "probabilities": {"billing": 0.34, "technical": 0.33, "account": 0.2, "off_topic": 0.13},
                "confidence": 0.2,
            }
        ),
        "severity": parse_answer(
            {
                "type": "score",
                "score": 0.4,
                "legend": {"0": "Calm", "1": "Frustrated", "2": "Abusive"},
                "probabilities": {"0": 0.7, "1": 0.2, "2": 0.1},
                "confidence": 0.6,
            }
        ),
        "needs_human": parse_answer({"type": "noul", "noul": 0.1}),
    }
    decision = compose_bot_action(answers)
    assert decision["action"] == "escalate"
    assert decision["template_id"] == "human_handoff"
    assert decision["reply"]


def test_bot_run_uses_shipped_path() -> None:
    def transport(payload: dict, api_key: str) -> dict:
        assert _types(payload["questions"]) == {"choice", "score", "noul"}
        return {
            "model": "jev-latest",
            "answers": {
                "intent": {
                    "type": "choice",
                    "choice": "technical",
                    "probabilities": {"billing": 0.05, "technical": 0.9, "account": 0.03, "off_topic": 0.02},
                    "confidence": 0.8,
                },
                "severity": {
                    "type": "score",
                    "score": 0.2,
                    "legend": {"0": "Calm", "1": "Frustrated", "2": "Abusive"},
                    "probabilities": {"0": 0.85, "1": 0.1, "2": 0.05},
                    "confidence": 0.7,
                },
                "needs_human": {"type": "noul", "noul": 0.1},
            },
            "usage": {"input_tokens": 1, "output_tokens": 1},
        }

    result = run_bot("stripe down", api_key="test-key", transport=transport)
    assert result["decision"]["action"] == "reply"
    assert result["decision"]["intent"] == "technical"
    assert result["decision"]["template_id"] == "tech_help"


def test_harness_rejects_off_task_delete() -> None:
    answers = {
        "verdict": parse_answer(
            {
                "type": "choice",
                "choice": "deny",
                "probabilities": {"allow": 0.05, "ask": 0.1, "deny": 0.85},
                "confidence": 0.8,
            }
        ),
        "irreversible": parse_answer(
            {
                "type": "score",
                "score": 2.0,
                "legend": {"0": "a", "1": "b", "2": "c"},
                "probabilities": {"0": 0.05, "1": 0.1, "2": 0.85},
                "confidence": 0.75,
            }
        ),
        "on_task": parse_answer({"type": "noul", "noul": 0.1}),
    }
    decision = compose_harness_gate(answers)
    assert decision["action"] == "reject"


def test_harness_run_confirms_high_stakes() -> None:
    def transport(payload: dict, api_key: str) -> dict:
        return {
            "model": "jev-latest",
            "answers": {
                "verdict": {
                    "type": "choice",
                    "choice": "ask",
                    "probabilities": {"allow": 0.2, "ask": 0.7, "deny": 0.1},
                    "confidence": 0.7,
                },
                "irreversible": {
                    "type": "score",
                    "score": 1.8,
                    "legend": {"0": "a", "1": "b", "2": "c"},
                    "probabilities": {"0": 0.1, "1": 0.2, "2": 0.7},
                    "confidence": 0.6,
                },
                "on_task": {"type": "noul", "noul": 0.8},
            },
            "usage": {},
        }

    result = run_harness("delete src", api_key="test-key", transport=transport)
    assert result["decision"]["action"] == "confirm"


def test_code_blocks_sql_injection_diff() -> None:
    answers = {
        "review": parse_answer(
            {
                "type": "choice",
                "choice": "request_changes",
                "probabilities": {"approve": 0.05, "comment": 0.1, "request_changes": 0.85},
                "confidence": 0.82,
            }
        ),
        "risk": parse_answer(
            {
                "type": "score",
                "score": 2.8,
                "legend": {"0": "a", "1": "b", "2": "c", "3": "d"},
                "probabilities": {"0": 0.02, "1": 0.05, "2": 0.13, "3": 0.8},
                "confidence": 0.77,
            }
        ),
        "tests_missing": parse_answer({"type": "noul", "noul": 0.9}),
    }
    decision = compose_review_gate(answers)
    assert decision["gate"] == "block"
    assert decision["review"] == "request_changes"


def test_code_run_shipped_evaluate() -> None:
    def transport(payload: dict, api_key: str) -> dict:
        assert "review" in payload["questions"]
        return {
            "model": "jev-latest",
            "answers": {
                "review": {
                    "type": "choice",
                    "choice": "approve",
                    "probabilities": {"approve": 0.9, "comment": 0.08, "request_changes": 0.02},
                    "confidence": 0.84,
                },
                "risk": {
                    "type": "score",
                    "score": 0.1,
                    "legend": {"0": "a", "1": "b", "2": "c", "3": "d"},
                    "probabilities": {"0": 0.9, "1": 0.07, "2": 0.02, "3": 0.01},
                    "confidence": 0.8,
                },
                "tests_missing": {"type": "noul", "noul": 0.05},
            },
            "usage": {},
        }

    result = run_code("docs typo", api_key="test-key", transport=transport)
    assert result["decision"]["gate"] == "merge"

"""Evaluate-and-compose path: shipped evaluate() + composer, fake transport only."""

from __future__ import annotations

from jev_master.apps.ticket_router import run_ticket
from jev_master.client import build_systemone_payload
from jev_master.apps.ticket_router import mixed_ticket_questions


def _real_shaped_body() -> dict:
    return {
        "model": "jev-latest",
        "answers": {
            "department": {
                "type": "choice",
                "choice": "technical",
                "probabilities": {"billing": 0.08, "technical": 0.85, "sales": 0.07},
                "confidence": 0.82,
            },
            "frustration": {
                "type": "score",
                "score": 1.6,
                "legend": {
                    "0": "Calm, just stating facts",
                    "1": "Frustrated but civil",
                    "2": "Very angry, strong language",
                },
                "probabilities": {"0": 0.05, "1": 0.3, "2": 0.65},
                "confidence": 0.78,
            },
            "is_urgent": {"type": "noul", "noul": 0.92},
        },
        "usage": {"input_tokens": 312, "output_tokens": 48},
    }


def test_run_ticket_uses_shipped_builder_and_returns_decision() -> None:
    seen = {}

    def transport(payload: dict, api_key: str) -> dict:
        seen["payload"] = payload
        seen["key_set"] = bool(api_key)
        types = {q["type"] for q in payload["questions"].values()}
        assert types == {"choice", "score", "noul"}
        return _real_shaped_body()

    result = run_ticket(
        "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing.",
        api_key="not-a-real-key",
        transport=transport,
    )
    expected = build_systemone_payload(
        "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing.",
        mixed_ticket_questions(),
    )
    assert seen["payload"]["questions"] == expected["questions"]
    assert seen["payload"]["model"] == "jev-latest"
    assert result["answers"]["department"]["choice"] == "technical"
    assert result["answers"]["department"]["probabilities"]
    assert abs(sum(result["answers"]["department"]["probabilities"].values()) - 1.0) < 1e-6
    assert result["answers"]["frustration"]["legend"]
    assert 0.0 <= result["answers"]["is_urgent"]["noul"] <= 1.0
    assert result["decision"]["department"] == "technical"
    assert result["decision"]["action"] in {"escalate", "act"}
    assert result["decision"]["handler"]
    assert result["decision"]["action"] != ""
    # Decision is structured fields, not generated prose.
    assert isinstance(result["decision"], dict)

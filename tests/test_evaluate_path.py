"""Evaluate-and-compose path: shipped evaluate() + composer, fake transport only."""

from __future__ import annotations

from jev_master.answers import parse_systemone_response
from jev_master.apps.confidence_gate import compose_confidence_gate, gate_questions, run_gate
from jev_master.apps.pitch_score import compose_pitch_score, pitch_questions, run_pitch
from jev_master.apps.ticket_router import mixed_ticket_questions, run_ticket
from jev_master.client import build_systemone_payload


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


def test_run_gate_uses_shipped_builder_and_composer() -> None:
    body = {
        "model": "jev-latest",
        "answers": {
            "intent": {
                "type": "choice",
                "choice": "check_balance",
                "probabilities": {"check_balance": 0.92, "approve_transfer": 0.05, "other": 0.03},
                "confidence": 0.81,
            },
            "stakes": {
                "type": "score",
                "score": 0.1,
                "legend": {"0": "low", "1": "mid", "2": "high"},
                "probabilities": {"0": 0.9, "1": 0.08, "2": 0.02},
                "confidence": 0.85,
            },
            "is_explicit": {"type": "noul", "noul": 0.4},
        },
        "usage": {"input_tokens": 10, "output_tokens": 4},
    }
    seen: dict = {}

    def transport(payload: dict, api_key: str) -> dict:
        seen["payload"] = payload
        types = {q["type"] for q in payload["questions"].values()}
        assert types == {"choice", "score", "noul"}
        return body

    result = run_gate("yeah go ahead and send the pending transfer", api_key="test-key", transport=transport)
    assert seen["payload"] == build_systemone_payload(
        "yeah go ahead and send the pending transfer",
        gate_questions(),
    )
    expected = compose_confidence_gate(parse_systemone_response(body).answers)
    assert result["decision"] == expected
    assert result["decision"]["action"] == "act"


def test_run_pitch_uses_shipped_builder_and_composer() -> None:
    body = {
        "model": "jev-latest",
        "answers": {
            "market": {
                "type": "score",
                "score": 2.4,
                "legend": {"0": "a", "1": "b", "2": "c", "3": "d"},
                "probabilities": {"0": 0.05, "1": 0.1, "2": 0.3, "3": 0.55},
                "confidence": 0.7,
            },
            "feasibility": {
                "type": "score",
                "score": 2.1,
                "legend": {"0": "a", "1": "b", "2": "c", "3": "d"},
                "probabilities": {"0": 0.05, "1": 0.15, "2": 0.4, "3": 0.4},
                "confidence": 0.66,
            },
            "differentiation": {
                "type": "score",
                "score": 1.8,
                "legend": {"0": "a", "1": "b", "2": "c", "3": "d"},
                "probabilities": {"0": 0.1, "1": 0.2, "2": 0.5, "3": 0.2},
                "confidence": 0.6,
            },
            "stage": {
                "type": "choice",
                "choice": "pre_seed",
                "probabilities": {"pre_seed": 0.8, "seed": 0.15, "series_a": 0.05},
                "confidence": 0.72,
            },
            "has_traction": {"type": "noul", "noul": 0.91},
        },
        "usage": {},
    }
    seen: dict = {}

    def transport(payload: dict, api_key: str) -> dict:
        seen["payload"] = payload
        types = {q["type"] for q in payload["questions"].values()}
        assert types == {"choice", "score", "noul"}
        return body

    result = run_pitch("Relays HVAC marketplace pitch", api_key="test-key", transport=transport)
    assert seen["payload"] == build_systemone_payload("Relays HVAC marketplace pitch", pitch_questions())
    expected = compose_pitch_score(parse_systemone_response(body).answers)
    assert result["decision"] == expected
    assert result["decision"]["verdict"] in {"pass", "hold", "reject"}

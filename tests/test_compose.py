"""Drive shipped composers with real-shaped System One answers."""

from __future__ import annotations

from jev_master.answers import parse_answer
from jev_master.apps.confidence_gate import compose_confidence_gate
from jev_master.apps.pitch_score import compose_pitch_score
from jev_master.apps.ticket_router import compose_ticket_route


def _choice(choice: str, probs: dict[str, float], confidence: float):
    return parse_answer(
        {
            "type": "choice",
            "choice": choice,
            "probabilities": probs,
            "confidence": confidence,
        }
    )


def _score(score: float, legend: dict[str, str], probs: dict[str, float], confidence: float):
    return parse_answer(
        {
            "type": "score",
            "score": score,
            "legend": legend,
            "probabilities": probs,
            "confidence": confidence,
        }
    )


def _noul(value: float):
    return parse_answer({"type": "noul", "noul": value})


def test_ticket_route_escalates_urgent_angry_technical() -> None:
    answers = {
        "department": _choice(
            "technical",
            {"billing": 0.08, "technical": 0.85, "sales": 0.07},
            0.82,
        ),
        "frustration": _score(
            1.8,
            {
                "0": "Calm, just stating facts",
                "1": "Frustrated but civil",
                "2": "Very angry, strong language",
            },
            {"0": 0.05, "1": 0.15, "2": 0.80},
            0.78,
        ),
        "is_urgent": _noul(0.99),
    }
    decision = compose_ticket_route(answers)
    assert decision["department"] == "technical"
    assert decision["action"] == "escalate"
    assert decision["handler"]
    assert decision["action"] in {"escalate", "act"}


def test_ticket_route_acts_on_calm_billing() -> None:
    answers = {
        "department": _choice(
            "billing",
            {"billing": 0.9, "technical": 0.05, "sales": 0.05},
            0.84,
        ),
        "frustration": _score(
            0.2,
            {"0": "Calm", "1": "Frustrated", "2": "Angry"},
            {"0": 0.85, "1": 0.10, "2": 0.05},
            0.80,
        ),
        "is_urgent": _noul(0.1),
    }
    decision = compose_ticket_route(answers)
    assert decision["department"] == "billing"
    assert decision["action"] == "act"
    assert "billing" in decision["handler"]


def test_ticket_route_low_confidence_escalates() -> None:
    answers = {
        "department": _choice(
            "sales",
            {"billing": 0.34, "technical": 0.33, "sales": 0.33},
            0.21,
        ),
        "frustration": _score(1.0, {"0": "a", "1": "b", "2": "c"}, {"0": 0.3, "1": 0.4, "2": 0.3}, 0.4),
        "is_urgent": _noul(0.5),
    }
    decision = compose_ticket_route(answers)
    assert decision["action"] == "escalate"
    assert decision["handler"] == "human_triage"


def test_confidence_gate_escalates_below_floor() -> None:
    answers = {
        "intent": _choice(
            "approve_transfer",
            {"check_balance": 0.3, "approve_transfer": 0.4, "other": 0.3},
            0.22,
        ),
        "stakes": _score(2.0, {"0": "low", "1": "mid", "2": "high"}, {"0": 0.05, "1": 0.1, "2": 0.85}, 0.7),
        "is_explicit": _noul(0.9),
    }
    decision = compose_confidence_gate(answers)
    assert decision["action"] == "escalate"
    assert decision["intent"] == "approve_transfer"


def test_confidence_gate_acts_on_balance() -> None:
    answers = {
        "intent": _choice(
            "check_balance",
            {"check_balance": 0.92, "approve_transfer": 0.05, "other": 0.03},
            0.81,
        ),
        "stakes": _score(0.1, {"0": "low", "1": "mid", "2": "high"}, {"0": 0.9, "1": 0.08, "2": 0.02}, 0.85),
        "is_explicit": _noul(0.4),
    }
    decision = compose_confidence_gate(answers)
    assert decision["action"] == "act"


def test_pitch_score_returns_numeric_composite_and_verdict() -> None:
    answers = {
        "market": _score(2.4, {"0": "a", "1": "b", "2": "c", "3": "d"}, {"0": 0.05, "1": 0.1, "2": 0.3, "3": 0.55}, 0.7),
        "feasibility": _score(2.1, {"0": "a", "1": "b", "2": "c", "3": "d"}, {"0": 0.05, "1": 0.15, "2": 0.4, "3": 0.4}, 0.66),
        "differentiation": _score(1.8, {"0": "a", "1": "b", "2": "c", "3": "d"}, {"0": 0.1, "1": 0.2, "2": 0.5, "3": 0.2}, 0.6),
        "stage": _choice(
            "pre_seed",
            {"pre_seed": 0.8, "seed": 0.15, "series_a": 0.05},
            0.72,
        ),
        "has_traction": _noul(0.91),
    }
    decision = compose_pitch_score(answers)
    assert isinstance(decision["composite"], float)
    assert 0.0 <= decision["composite"] <= 1.0
    assert decision["verdict"] in {"pass", "hold", "reject"}
    assert decision["stage"] == "pre_seed"
    assert decision["composite"] > 0

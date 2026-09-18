"""Drive the shipped request builder. Mixed Choice + Score + Noul in one payload."""

from __future__ import annotations

from jev_master.apps.confidence_gate import gate_questions
from jev_master.apps.jev_bot import bot_questions
from jev_master.apps.jev_code import code_questions
from jev_master.apps.jev_harness import harness_questions
from jev_master.apps.pitch_score import pitch_questions
from jev_master.apps.ticket_router import mixed_ticket_questions
from jev_master.client import DEFAULT_MODEL, SYSTEMONE_URL, build_systemone_payload

FAMILY_BUILDERS = (
    mixed_ticket_questions,
    gate_questions,
    pitch_questions,
    bot_questions,
    harness_questions,
    code_questions,
)


def test_systemone_url_and_model() -> None:
    assert SYSTEMONE_URL == "https://api.typesafe.ai/v1/systemone"
    payload = build_systemone_payload("state", mixed_ticket_questions())
    assert payload["model"] == "jev-latest"
    assert payload["model"] == DEFAULT_MODEL


def test_mixed_payload_contains_choice_score_noul() -> None:
    questions = mixed_ticket_questions()
    payload = build_systemone_payload(
        "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing.",
        questions,
    )
    types = {item["type"] for item in payload["questions"].values()}
    assert types == {"choice", "score", "noul"}
    assert payload["questions"]["department"]["type"] == "choice"
    assert payload["questions"]["frustration"]["type"] == "score"
    assert payload["questions"]["is_urgent"]["type"] == "noul"
    assert "billing" in payload["questions"]["department"]["criteria"]
    assert len(payload["questions"]["frustration"]["criteria"]) >= 2
    assert "instructions" in payload["questions"]["is_urgent"]


def test_payload_preserves_state_and_question_ids() -> None:
    questions = mixed_ticket_questions()
    payload = build_systemone_payload({"ticket": "help"}, questions)
    assert payload["state"] == {"ticket": "help"}
    assert set(payload["questions"]) == {"department", "frustration", "is_urgent"}


def test_family_builders_mix_choice_score_noul() -> None:
    for builder in FAMILY_BUILDERS:
        payload = build_systemone_payload("state", builder())
        types = {item["type"] for item in payload["questions"].values()}
        assert types == {"choice", "score", "noul"}, builder.__name__
        assert payload["model"] == "jev-latest"
        assert payload["model"] == DEFAULT_MODEL

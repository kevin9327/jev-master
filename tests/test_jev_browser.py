"""Drive JevBrowser through shipped builders and composers — no theater."""

from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request
from typing import Any

from jev_master.answers import parse_systemone_response
from jev_master.apps.jev_browser import (
    evaluate_body,
    make_server,
    playground_payload,
    resolve_static_dir,
)
from jev_master.apps.ticket_router import compose_ticket_route, mixed_ticket_questions
from jev_master.client import build_systemone_payload

STATE = "Hi, I've been trying to connect my Stripe account for 3 days."
FAKE_CHOICE = "technical"

FAKE_RAW: dict[str, Any] = {
    "model": "jev-latest",
    "answers": {
        "department": {
            "type": "choice",
            "choice": FAKE_CHOICE,
            "probabilities": {"billing": 0.04, "technical": 0.91, "sales": 0.05},
            "confidence": 0.77,
        },
        "frustration": {
            "type": "score",
            "score": 1.4,
            "legend": {
                "0": "Calm, just stating facts",
                "1": "Frustrated but civil",
                "2": "Very angry, strong language",
            },
            "probabilities": {"0": 0.1, "1": 0.55, "2": 0.35},
            "confidence": 0.8,
        },
        "is_urgent": {"type": "noul", "noul": 0.93},
    },
    "usage": {"input_tokens": 20, "output_tokens": 6},
}


def test_mixed_payload_uses_shipped_builder_choice_score_noul() -> None:
    payload = playground_payload(STATE, "mixed")
    expected = build_systemone_payload(STATE, mixed_ticket_questions())
    assert payload == expected
    types = {question["type"] for question in payload["questions"].values()}
    assert types == {"choice", "score", "noul"}
    assert payload["model"] == "jev-latest"


def test_fake_transport_composes_nonempty_decision_via_shipped_composer() -> None:
    seen: dict[str, Any] = {}

    def transport(payload: dict[str, Any], api_key: str) -> dict[str, Any]:
        seen["payload"] = payload
        seen["api_key"] = api_key
        return FAKE_RAW

    result = evaluate_body(
        {"state": STATE, "app": "mixed"},
        api_key="test-key",
        transport=transport,
    )
    questions = seen["payload"]["questions"]
    assert {q["type"] for q in questions.values()} == {"choice", "score", "noul"}
    assert seen["payload"] == build_systemone_payload(STATE, mixed_ticket_questions())

    parsed = parse_systemone_response(FAKE_RAW)
    expected = compose_ticket_route(parsed.answers)
    assert result["decision"] == expected
    assert result["decision"]
    assert result["decision"]["department"] == FAKE_CHOICE
    assert not isinstance(result["decision"], str)
    assert result["answers"]["department"]["choice"] == FAKE_CHOICE


def test_http_handler_evaluate_and_static() -> None:
    def transport(payload: dict[str, Any], api_key: str) -> dict[str, Any]:
        return FAKE_RAW

    httpd = make_server(
        "127.0.0.1",
        0,
        static_dir=resolve_static_dir(),
        transport=transport,
        key_loader=lambda: "test-key",
    )
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        port = httpd.server_address[1]
        page = urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5).read().decode("utf-8")
        assert "JevBrowser" in page
        assert "jev-latest" in page
        assert "POST /v1/systemone" in page
        assert "TYPESAFE_API_KEY" not in page
        assert "jevkey" not in page.lower()

        req = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/evaluate",
            data=json.dumps({"state": STATE, "app": "mixed"}).encode("utf-8"),
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raise AssertionError(exc.read().decode("utf-8", errors="replace")) from exc
        expected = compose_ticket_route(parse_systemone_response(FAKE_RAW).answers)
        assert body["decision"] == expected
        assert body["decision"]
        assert body["answers"]
    finally:
        httpd.shutdown()
        httpd.server_close()


def test_static_has_no_api_key() -> None:
    static = resolve_static_dir()
    blob = "".join(path.read_text(encoding="utf-8") for path in static.iterdir() if path.is_file())
    assert "TYPESAFE_API_KEY" not in blob
    assert "jevkey" not in blob.lower()
    assert "sk-" not in blob

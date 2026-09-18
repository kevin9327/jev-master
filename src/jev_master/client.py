"""Thin System One HTTP client. Builds the request; does not compose decisions."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any

from jev_master.answers import SystemOneResult, parse_systemone_response

SYSTEMONE_URL = "https://api.typesafe.ai/v1/systemone"
DEFAULT_MODEL = "jev-latest"

Transport = Callable[[dict[str, Any], str], dict[str, Any]]


class SystemOneError(RuntimeError):
    def __init__(self, status: int, body: str) -> None:
        self.status = status
        self.body = body
        super().__init__(f"System One HTTP {status}: {body[:500]}")


def choice_question(instructions: str, criteria: Mapping[str, str | None]) -> dict[str, Any]:
    return {"type": "choice", "instructions": instructions, "criteria": dict(criteria)}


def score_question(instructions: str, criteria: list[str]) -> dict[str, Any]:
    if len(criteria) < 2:
        raise ValueError("Score questions need at least two criteria levels")
    return {"type": "score", "instructions": instructions, "criteria": list(criteria)}


def noul_question(
    instructions: str, criteria: Mapping[str, str] | None = None
) -> dict[str, Any]:
    question: dict[str, Any] = {"type": "noul", "instructions": instructions}
    if criteria:
        question["criteria"] = dict(criteria)
    return question


def build_systemone_payload(
    state: str | dict[str, Any] | list[Any],
    questions: Mapping[str, Mapping[str, Any]],
    model: str = DEFAULT_MODEL,
) -> dict[str, Any]:
    """Build the JSON body for POST /v1/systemone. Tests assert this shape."""
    if not questions:
        raise ValueError("questions must not be empty")
    return {
        "state": state,
        "model": model,
        "questions": {key: dict(value) for key, value in questions.items()},
    }


def post_systemone(
    payload: dict[str, Any],
    api_key: str,
    *,
    timeout: float = 60.0,
    retries: int = 3,
) -> dict[str, Any]:
    if not api_key or not api_key.strip():
        raise SystemOneError(401, "missing API key")
    data = json.dumps(payload).encode("utf-8")
    last_error: Exception | None = None
    for attempt in range(retries):
        request = urllib.request.Request(
            SYSTEMONE_URL,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key.strip()}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "jev-master/0.1",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in (429, 529) and attempt + 1 < retries:
                time.sleep(2**attempt)
                last_error = SystemOneError(exc.code, body)
                continue
            raise SystemOneError(exc.code, body) from exc
        except urllib.error.URLError as exc:
            raise SystemOneError(0, f"connection failed: {exc.reason}") from exc
    assert last_error is not None
    raise last_error


def evaluate(
    state: str | dict[str, Any] | list[Any],
    questions: Mapping[str, Mapping[str, Any]],
    *,
    api_key: str,
    model: str = DEFAULT_MODEL,
    transport: Transport | None = None,
) -> SystemOneResult:
    payload = build_systemone_payload(state, questions, model=model)
    raw = (transport or post_systemone)(payload, api_key)
    return parse_systemone_response(raw)

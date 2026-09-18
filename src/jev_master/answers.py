"""Parse typed System One answers. No prose is treated as a decision."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ChoiceAnswer:
    type: str
    choice: str
    probabilities: dict[str, float]
    confidence: float

    def __post_init__(self) -> None:
        if self.type != "choice":
            raise ValueError(f"expected type=choice, got {self.type}")
        if not self.choice:
            raise ValueError("choice answer is empty")
        if not self.probabilities:
            raise ValueError("choice probabilities missing")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("choice confidence must be in [0, 1]")


@dataclass(frozen=True)
class ScoreAnswer:
    type: str
    score: float
    legend: dict[str, str]
    probabilities: dict[str, float]
    confidence: float

    def __post_init__(self) -> None:
        if self.type != "score":
            raise ValueError(f"expected type=score, got {self.type}")
        if not self.legend:
            raise ValueError("score legend missing")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("score confidence must be in [0, 1]")


@dataclass(frozen=True)
class NoulAnswer:
    type: str
    noul: float

    def __post_init__(self) -> None:
        if self.type != "noul":
            raise ValueError(f"expected type=noul, got {self.type}")
        if not 0.0 <= self.noul <= 1.0:
            raise ValueError("noul must be in [0, 1]")


Answer = ChoiceAnswer | ScoreAnswer | NoulAnswer


@dataclass(frozen=True)
class SystemOneResult:
    model: str
    answers: dict[str, Answer]
    usage: dict[str, int]
    raw: dict[str, Any]


def _as_float_map(value: Any, field: str) -> dict[str, float]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return {str(key): float(item) for key, item in value.items()}


def parse_answer(payload: dict[str, Any]) -> Answer:
    kind = payload.get("type")
    if kind == "choice":
        return ChoiceAnswer(
            type="choice",
            choice=str(payload["choice"]),
            probabilities=_as_float_map(payload.get("probabilities"), "probabilities"),
            confidence=float(payload["confidence"]),
        )
    if kind == "score":
        legend = payload.get("legend") or {}
        if not isinstance(legend, dict):
            raise ValueError("score legend must be an object")
        probabilities = payload.get("probabilities") or {}
        return ScoreAnswer(
            type="score",
            score=float(payload["score"]),
            legend={str(key): str(item) for key, item in legend.items()},
            probabilities=_as_float_map(probabilities, "score probabilities"),
            confidence=float(payload["confidence"]),
        )
    if kind == "noul":
        return NoulAnswer(type="noul", noul=float(payload["noul"]))
    raise ValueError(f"unknown answer type: {kind!r}")


def parse_systemone_response(body: dict[str, Any]) -> SystemOneResult:
    answers_raw = body.get("answers")
    if not isinstance(answers_raw, dict) or not answers_raw:
        raise ValueError("System One response is missing answers")
    answers = {key: parse_answer(value) for key, value in answers_raw.items()}
    usage = body.get("usage") or {}
    return SystemOneResult(
        model=str(body.get("model") or "jev-latest"),
        answers=answers,
        usage={str(key): int(value) for key, value in usage.items()},
        raw=body,
    )


def answers_as_json(answers: dict[str, Answer]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, answer in answers.items():
        if isinstance(answer, ChoiceAnswer):
            out[key] = {
                "type": "choice",
                "choice": answer.choice,
                "probabilities": answer.probabilities,
                "confidence": answer.confidence,
            }
        elif isinstance(answer, ScoreAnswer):
            out[key] = {
                "type": "score",
                "score": answer.score,
                "legend": answer.legend,
                "probabilities": answer.probabilities,
                "confidence": answer.confidence,
            }
        else:
            out[key] = {"type": "noul", "noul": answer.noul}
    return out

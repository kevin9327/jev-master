"""Composite scoring: atomic scores combined with weights the code owns.

Pattern: https://docs.typesafe.ai/patterns/composite-scoring
The intro warns not to ask 'rate this startup pitch' as one question.
"""

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
Pitch: Relays is a marketplace that matches independent HVAC techs with
building managers in rust-belt cities. We have 40 paying buildings in
Cleveland, $18k MRR, and a two-sided waitlist in Detroit. Moat is local
dispatch density plus a licensed-tech network, not a model. Raising a
$1.2M pre-seed to hire two ops leads and expand to Pittsburgh.
"""

WEIGHTS = {
    "market": 0.35,
    "feasibility": 0.30,
    "differentiation": 0.25,
    "traction": 0.10,
}


def pitch_questions() -> dict[str, dict[str, Any]]:
    return {
        "market": score_question(
            "How large and reachable is the stated market, given only this pitch?",
            [
                "No market or a hobby niche",
                "Small local market with unclear expansion",
                "Clear regional market",
                "Large market with a credible wedge",
            ],
        ),
        "feasibility": score_question(
            "How technically and operationally feasible is this plan as written?",
            [
                "Depends on unstated magic",
                "Possible but thin on how",
                "Credible ops plan with known constraints",
                "Team already executing the hard parts",
            ],
        ),
        "differentiation": score_question(
            "How distinct is the wedge versus a generic marketplace?",
            [
                "Undifferentiated 'Uber for X'",
                "Some local color, easy to copy",
                "A specific density or network effect",
                "Hard-to-copy asset already forming",
            ],
        ),
        "stage": choice_question(
            "Which financing stage does this pitch match?",
            {
                "pre_seed": "Idea or early revenue, raising to find a motion",
                "seed": "Repeatable motion, raising to scale a channel",
                "series_a": "Proven engine, raising to expand a machine",
            },
        ),
        "has_traction": noul_question(
            "The pitch cites concrete paying customers or revenue, not just interest",
        ),
    }


def compose_pitch_score(answers: dict[str, Any]) -> dict[str, Any]:
    market = answers["market"]
    feasibility = answers["feasibility"]
    differentiation = answers["differentiation"]
    stage = answers["stage"]
    has_traction = answers["has_traction"]
    if not all(isinstance(item, ScoreAnswer) for item in (market, feasibility, differentiation)):
        raise TypeError("market, feasibility, and differentiation must be ScoreAnswers")
    if not isinstance(stage, ChoiceAnswer):
        raise TypeError("stage must be a ChoiceAnswer")
    if not isinstance(has_traction, NoulAnswer):
        raise TypeError("has_traction must be a NoulAnswer")

    # Score criteria have 4 levels (0..3). Normalize to 0..1, then weight.
    traction = has_traction.noul
    parts = {
        "market": market.score / 3.0,
        "feasibility": feasibility.score / 3.0,
        "differentiation": differentiation.score / 3.0,
        "traction": traction,
    }
    composite = sum(WEIGHTS[name] * parts[name] for name in WEIGHTS)
    if composite >= 0.72 and has_traction.noul >= 0.6:
        verdict = "pass"
    elif composite >= 0.45:
        verdict = "hold"
    else:
        verdict = "reject"

    return {
        "composite": round(composite, 4),
        "verdict": verdict,
        "stage": stage.choice,
        "parts": {key: round(value, 4) for key, value in parts.items()},
        "weights": dict(WEIGHTS),
        "confidence": min(market.confidence, feasibility.confidence, differentiation.confidence, stage.confidence),
    }


def run_pitch(
    state: str,
    *,
    api_key: str = "test-key",
    transport: Transport | None = None,
) -> dict[str, Any]:
    result = evaluate(state, pitch_questions(), api_key=api_key, transport=transport)
    decision = compose_pitch_score(result.answers)
    return {
        "app": "pitch_score",
        "pattern": "composite-scoring",
        "model": result.model,
        "state": state,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Composite-score a startup pitch with Jev")
    parser.add_argument("--state", help="Path to a state file")
    parser.add_argument("--text", help="Inline state text")
    args = parser.parse_args(argv)
    state = args.text if args.text else (
        Path(args.state).read_text(encoding="utf-8").strip() if args.state else SAMPLE_STATE
    )
    json.dump(run_pitch(state, api_key=load_api_key()), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

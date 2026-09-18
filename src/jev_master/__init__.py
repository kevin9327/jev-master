"""jev-master: typed System One decisions composed in code."""

from jev_master.answers import ChoiceAnswer, NoulAnswer, ScoreAnswer, parse_systemone_response
from jev_master.client import (
    SYSTEMONE_URL,
    build_systemone_payload,
    choice_question,
    evaluate,
    noul_question,
    score_question,
)

__all__ = [
    "SYSTEMONE_URL",
    "ChoiceAnswer",
    "NoulAnswer",
    "ScoreAnswer",
    "build_systemone_payload",
    "choice_question",
    "evaluate",
    "noul_question",
    "parse_systemone_response",
    "score_question",
]

__version__ = "0.1.0"

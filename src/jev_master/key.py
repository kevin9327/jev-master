"""Load TYPESAFE_API_KEY from the environment. Optional local file, never copied in."""

from __future__ import annotations

import os
from pathlib import Path

DEFAULT_KEY_FILE = Path(r"C:\Users\swsz9\Downloads\jevkey.txt")
ENV_NAME = "TYPESAFE_API_KEY"


def load_api_key(*, key_file: Path | None = None, environ: dict[str, str] | None = None) -> str:
    env = environ if environ is not None else os.environ
    value = (env.get(ENV_NAME) or "").strip()
    if value:
        return value
    path = key_file if key_file is not None else DEFAULT_KEY_FILE
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    raise RuntimeError(
        f"{ENV_NAME} is not set and no key file was found at {path}. "
        "Export the key or place it outside this repository."
    )

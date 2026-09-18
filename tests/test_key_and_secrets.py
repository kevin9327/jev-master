"""Key loader stays out of the tree; gitignore covers secret names."""

from __future__ import annotations

import re
from pathlib import Path

from jev_master.key import ENV_NAME, load_api_key

ROOT = Path(__file__).resolve().parents[1]
# Split so this test file does not itself contain a key-shaped assignment.
KEY_SHAPE = re.compile("api" + r"key_[A-Za-z0-9]{8,}")
ASSIGNED_ENV = re.compile("TYPESAFE_API_KEY" + r"=\S+")


def test_load_api_key_from_environ() -> None:
    assert load_api_key(environ={ENV_NAME: "  test-key-not-for-commit  "}, key_file=Path("missing")) == "test-key-not-for-commit"


def test_gitignore_excludes_key_files() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "jevkey.txt" in text
    assert ".env" in text
    assert "apikey_*" in text


def test_tracked_tree_has_no_key_literals() -> None:
    hits: list[str] = []
    skip = {".git", ".venv", "__pycache__", ".pytest_cache"}
    for path in ROOT.rglob("*"):
        if any(part in skip for part in path.parts):
            continue
        if path.name == "test_key_and_secrets.py":
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if KEY_SHAPE.search(text) or ASSIGNED_ENV.search(text):
            hits.append(str(path.relative_to(ROOT)))
    assert hits == []

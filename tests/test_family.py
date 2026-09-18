"""Family integration: CLI launch names, README, shipped builders/composers."""

from __future__ import annotations

import json
from pathlib import Path

from jev_master.catalog import github_urls
from jev_master.cli import APPS, COMPOSE_APPS, main

ROOT = Path(__file__).resolve().parents[1]


def test_compose_apps_are_independently_launchable() -> None:
    assert COMPOSE_APPS == ("ticket", "gate", "pitch", "bot", "harness", "code")
    for name in COMPOSE_APPS:
        assert name in APPS


def test_cli_dispatches_each_compose_app(monkeypatch, capsys) -> None:
    import jev_master.cli as cli

    monkeypatch.setattr(cli, "load_api_key", lambda: "test-key")
    recorded: dict[str, tuple[str, str]] = {}

    def _runner(name: str):
        def run(state: str, *, api_key: str = "") -> dict:
            recorded[name] = (state, api_key)
            return {"app": name, "decision": {"ok": True}}

        return run

    monkeypatch.setattr(cli, "run_ticket", _runner("ticket"))
    monkeypatch.setattr(cli, "run_gate", _runner("gate"))
    monkeypatch.setattr(cli, "run_pitch", _runner("pitch"))
    monkeypatch.setattr(cli, "run_bot", _runner("bot"))
    monkeypatch.setattr(cli, "run_harness", _runner("harness"))
    monkeypatch.setattr(cli, "run_code", _runner("code"))

    for name in COMPOSE_APPS:
        recorded.clear()
        rc = main([name, "--text", f"state-{name}"])
        assert rc == 0
        assert recorded[name] == (f"state-{name}", "test-key")
        payload = json.loads(capsys.readouterr().out)
        assert payload["app"] == name
        assert payload["decision"]["ok"] is True


def test_readme_names_typesafe_jev_family() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for needle in (
        "TypeSafe",
        "Jev",
        "POST /v1/systemone",
        "Choice",
        "Score",
        "Noul",
        "python -m jev_master ticket",
        "python -m jev_master gate",
        "python -m jev_master pitch",
        "python -m jev_master bot",
        "python -m jev_master harness",
        "python -m jev_master code",
        "https://github.com/kevin9327/jev-bot",
        "https://github.com/kevin9327/jev-harness",
        "https://github.com/kevin9327/jev-code",
        "jev_bot",
        "jev_harness",
        "jev_code",
    ):
        assert needle in text, needle


def test_catalog_cites_sibling_family_repos() -> None:
    urls = github_urls()
    for url in (
        "https://github.com/kevin9327/jev-bot",
        "https://github.com/kevin9327/jev-harness",
        "https://github.com/kevin9327/jev-code",
        "https://github.com/kevin9327/jev-master",
    ):
        assert url in urls

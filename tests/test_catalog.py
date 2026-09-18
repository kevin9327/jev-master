"""Catalog is a citation index, not a vendor dump of other GitHub repos."""

from __future__ import annotations

from pathlib import Path

from jev_master.catalog import github_urls, load_catalog, render_markdown

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_has_many_unique_github_citations() -> None:
    data = load_catalog()
    urls = github_urls(data)
    assert len(data["entries"]) >= 60
    assert len(urls) >= 50
    assert len(set(urls)) == len(urls)
    kinds = {entry["kind"] for entry in data["entries"]}
    for required in ("official", "sdk", "agent", "browser", "app", "game", "research", "list", "x"):
        assert required in kinds
    patterns = {entry.get("pattern") for entry in data["entries"]}
    assert "intent-routing" in patterns
    assert "confidence-gate" in patterns
    assert "composite-score" in patterns


def test_catalog_does_not_clone_other_repos() -> None:
    for name in ("vendor", "awesome-jev", "third_party", "mirrors"):
        assert not (ROOT / name).exists()
    nested = [path for path in ROOT.rglob(".git") if path != ROOT / ".git"]
    assert nested == []


def test_render_markdown_says_cited_not_cloned() -> None:
    text = render_markdown()
    assert "not cloned" in text.lower() or "not vendor" in text.lower()
    assert "POST /v1/systemone" in text or "v1/systemone" in text or "compose" in text
    assert "https://github.com/typesafe-ai/typesafe-sdk-python" in text
    assert "https://github.com/browser-use/jev-ultrafast" in text

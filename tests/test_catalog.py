"""Catalog is a citation index, not a vendor dump of other GitHub repos."""

from __future__ import annotations

from pathlib import Path

from jev_master.catalog import github_urls, load_catalog, render_markdown

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_has_many_unique_github_citations() -> None:
    data = load_catalog()
    urls = [str(entry.get("url") or "") for entry in data["entries"]]
    github = github_urls(data)
    assert len(data["entries"]) > 88
    assert len(set(urls)) == len(urls)
    assert len(github) >= 50
    assert len(set(github)) == len(github)
    assert any("github.com/" in url for url in urls)
    assert any("x.com/" in url for url in urls)
    kinds = {entry["kind"] for entry in data["entries"]}
    for required in ("official", "sdk", "agent", "browser", "vision", "app", "game", "research", "list", "x"):
        assert required in kinds
    patterns = {entry.get("pattern") for entry in data["entries"]}
    assert "intent-routing" in patterns
    assert "confidence-gate" in patterns
    assert "composite-score" in patterns
    # 2026-09-19 harvest: previously missing user repo + new GitHub and X citations
    assert "https://github.com/kevin9327/jev-visual" in urls
    assert "https://github.com/githubnext/localjev" in urls
    assert "https://github.com/Davipar/djev-dev" in urls
    assert "https://github.com/mmastrac/djev-spark" in urls
    assert "https://github.com/Argos1111/jev_local" in urls
    assert "https://x.com/typesafeai/status/2100747035746193598" in urls
    assert "https://x.com/CompleteSkeptic/status/2099925682726002904" in urls
    assert "https://x.com/LukeberryPi/status/2101307264829149210" in urls


def test_catalog_does_not_clone_other_repos() -> None:
    for name in ("vendor", "awesome-jev", "third_party", "mirrors"):
        assert not (ROOT / name).exists()
    nested = [path for path in ROOT.rglob(".git") if path != ROOT / ".git"]
    assert nested == []
    assert not (ROOT / ".gitmodules").exists()
    # Shipped catalog is docs/ecosystem.json, not a vendored copy of other trees
    shipped = ROOT / "docs" / "ecosystem.json"
    assert shipped.is_file()
    assert load_catalog()["entries"] is not None
    text = shipped.read_text(encoding="utf-8")
    assert "https://github.com/kevin9327/jev-visual" in text


def test_render_markdown_says_cited_not_cloned() -> None:
    text = render_markdown()
    assert "not cloned" in text.lower() or "not vendor" in text.lower()
    assert "POST /v1/systemone" in text or "v1/systemone" in text or "compose" in text
    assert "https://github.com/typesafe-ai/typesafe-sdk-python" in text
    assert "https://github.com/browser-use/jev-ultrafast" in text
    assert "https://github.com/Davipar/djev-dev" in text
    assert "Vision, images, and local eyes" in text
    assert "JevBot" in text and "JevHarness" in text and "JevCode" in text
    assert "three compose apps" not in text

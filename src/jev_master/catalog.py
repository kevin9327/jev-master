"""Cited Jev / TypeSafe field map. Links only — nothing is vendored."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

KINDS = (
    "official",
    "sdk",
    "agent",
    "browser",
    "app",
    "game",
    "research",
    "list",
    "x",
)

PATTERNS = (
    "intent-routing",
    "confidence-gate",
    "composite-score",
    "fan-out",
    "client",
    "catalog",
    "other",
)


def catalog_path() -> Path:
    here = Path(__file__).resolve()
    candidates = [
        here.parents[2] / "docs" / "ecosystem.json",
        Path.cwd() / "docs" / "ecosystem.json",
    ]
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError("docs/ecosystem.json not found")


def load_catalog(path: Path | None = None) -> dict[str, Any]:
    data = json.loads((path or catalog_path()).read_text(encoding="utf-8"))
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("catalog entries missing")
    return data


def github_urls(data: dict[str, Any] | None = None) -> list[str]:
    payload = data or load_catalog()
    urls: list[str] = []
    seen: set[str] = set()
    for entry in payload["entries"]:
        url = str(entry.get("url") or "")
        if "github.com/" in url and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def render_markdown(data: dict[str, Any] | None = None) -> str:
    payload = data or load_catalog()
    lines = [
        "# Jev field map (cited, not cloned)",
        "",
        "This file is an index of public Jev / TypeSafe System One work.",
        "**We do not vendor, mirror, or submodule these repositories.**",
        "Star counts and trending rank are not claimed.",
        "",
        f"Surveyed {payload.get('surveyed')} · {len(payload['entries'])} cited entries · {payload.get('date')}.",
        "",
        "Sources we read (still not copied into this tree):",
        "",
    ]
    for source in payload.get("sources") or []:
        lines.append(f"- {source}")
    lines += [
        "",
        "Method: public GitHub READMEs + X posts. Inclusion is not TypeSafe affiliation.",
        "",
    ]
    by_kind: dict[str, list[dict[str, Any]]] = {kind: [] for kind in KINDS}
    for entry in payload["entries"]:
        kind = str(entry.get("kind") or "other")
        by_kind.setdefault(kind, []).append(entry)
    titles = {
        "official": "Official",
        "sdk": "SDKs and clients",
        "agent": "Agents, gates, MCP",
        "browser": "Browser and computer use",
        "app": "Applications",
        "game": "Games and simulations",
        "research": "Open replicas and evals",
        "list": "Other directories",
        "x": "X threads",
    }
    for kind in KINDS:
        rows = by_kind.get(kind) or []
        if not rows:
            continue
        lines.append(f"## {titles.get(kind, kind)}")
        lines.append("")
        for entry in rows:
            extra = f" — {entry['note']}" if entry.get("note") else ""
            pattern = entry.get("pattern")
            tag = f" `{pattern}`" if pattern else ""
            xurl = entry.get("x")
            xbit = f" · [X]({xurl})" if xurl else ""
            lines.append(f"- [{entry['name']}]({entry['url']}){tag}{extra}{xbit}")
        lines.append("")
    lines.append("## What jev-master adds")
    lines.append("")
    lines.append(
        "Link directories stop at the URL. This repo ships a live `POST /v1/systemone` "
        "client, mixed Choice+Score+Noul, compose apps (ticket/gate/pitch plus "
        "JevBot/JevHarness/JevCode), JevBrowser, and tests on the shipped builders "
        "— then points at the rest of the field."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print the cited Jev field map")
    parser.add_argument("--kind", choices=KINDS, help="Filter by kind")
    parser.add_argument("--json", action="store_true", help="Raw JSON entries")
    args = parser.parse_args(argv)
    data = load_catalog()
    entries = list(data["entries"])
    if args.kind:
        entries = [item for item in entries if item.get("kind") == args.kind]
    if args.json:
        json.dump(entries, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    print(f"{len(entries)} cited projects  (not cloned)")
    for entry in entries:
        print(f"{entry.get('kind'):10}  {entry['name']:28}  {entry['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

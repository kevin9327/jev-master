"""North-star CLI: python -m jev_master [ticket|gate|pitch|bot|harness|code]."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jev_master.apps.confidence_gate import SAMPLE_STATE as GATE_STATE
from jev_master.apps.confidence_gate import run_gate
from jev_master.apps.jev_bot import SAMPLE_STATE as BOT_STATE
from jev_master.apps.jev_bot import run_bot
from jev_master.apps.jev_code import SAMPLE_STATE as CODE_STATE
from jev_master.apps.jev_code import run_code
from jev_master.apps.jev_harness import SAMPLE_STATE as HARNESS_STATE
from jev_master.apps.jev_harness import run_harness
from jev_master.apps.pitch_score import SAMPLE_STATE as PITCH_STATE
from jev_master.apps.pitch_score import run_pitch
from jev_master.apps.ticket_router import SAMPLE_STATE as TICKET_STATE
from jev_master.apps.ticket_router import run_ticket
from jev_master.key import load_api_key

COMPOSE_APPS = ("ticket", "gate", "pitch", "bot", "harness", "code")
APPS = COMPOSE_APPS + ("browser", "catalog")


def _read_state(path: str | None, default: str) -> str:
    if not path:
        return default
    return Path(path).read_text(encoding="utf-8").strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="jev-master",
        description="Compose typed Jev (System One) answers into application decisions.",
    )
    parser.add_argument(
        "app",
        nargs="?",
        default="ticket",
        choices=APPS,
        help="Sub-project to launch (default: ticket mixed Choice+Score+Noul demo)",
    )
    parser.add_argument("--state", help="Path to a text/JSON state file")
    parser.add_argument("--text", help="Inline state text")
    parser.add_argument("--port", type=int, default=8765, help="JevBrowser bind port")
    parser.add_argument("--kind", help="catalog kind filter (sdk, browser, app, ...)")
    args = parser.parse_args(argv)

    if args.app == "browser":
        from jev_master.apps.jev_browser import main as browser_main

        return browser_main(["--port", str(args.port)])

    if args.app == "catalog":
        from jev_master.catalog import main as catalog_main

        extra: list[str] = []
        if args.kind:
            extra.extend(["--kind", args.kind])
        return catalog_main(extra)

    defaults = {
        "ticket": TICKET_STATE,
        "gate": GATE_STATE,
        "pitch": PITCH_STATE,
        "bot": BOT_STATE,
        "harness": HARNESS_STATE,
        "code": CODE_STATE,
    }
    if args.text:
        state = args.text
    else:
        state = _read_state(args.state, defaults[args.app])

    key = load_api_key()
    runners = {
        "ticket": run_ticket,
        "gate": run_gate,
        "pitch": run_pitch,
        "bot": run_bot,
        "harness": run_harness,
        "code": run_code,
    }
    payload = runners[args.app](state, api_key=key)

    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

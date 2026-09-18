"""North-star CLI: python -m jev_master [ticket|gate|pitch|browser]."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jev_master.apps.confidence_gate import SAMPLE_STATE as GATE_STATE
from jev_master.apps.confidence_gate import run_gate
from jev_master.apps.pitch_score import SAMPLE_STATE as PITCH_STATE
from jev_master.apps.pitch_score import run_pitch
from jev_master.apps.ticket_router import SAMPLE_STATE as TICKET_STATE
from jev_master.apps.ticket_router import run_ticket
from jev_master.key import load_api_key

APPS = ("ticket", "gate", "pitch", "browser")


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
    args = parser.parse_args(argv)

    if args.app == "browser":
        from jev_master.apps.jev_browser import main as browser_main

        return browser_main(["--port", str(args.port)])

    if args.text:
        state = args.text
    elif args.app == "ticket":
        state = _read_state(args.state, TICKET_STATE)
    elif args.app == "gate":
        state = _read_state(args.state, GATE_STATE)
    else:
        state = _read_state(args.state, PITCH_STATE)

    key = load_api_key()
    if args.app == "ticket":
        payload = run_ticket(state, api_key=key)
    elif args.app == "gate":
        payload = run_gate(state, api_key=key)
    else:
        payload = run_pitch(state, api_key=key)

    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

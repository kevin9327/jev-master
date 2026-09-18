"""Launch JevBrowser: python apps/jev_browser"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from jev_master.apps.jev_browser import main

if __name__ == "__main__":
    raise SystemExit(main())

"""Local JevBrowser playground: inspect Choice+Score+Noul, compose in code.

Stdlib HTTP only. Static UI lives in apps/jev_browser/static.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from jev_master.answers import answers_as_json
from jev_master.apps.confidence_gate import compose_confidence_gate, gate_questions
from jev_master.apps.pitch_score import compose_pitch_score, pitch_questions
from jev_master.apps.ticket_router import compose_ticket_route, mixed_ticket_questions
from jev_master.client import (
    DEFAULT_MODEL,
    SYSTEMONE_URL,
    SystemOneError,
    Transport,
    build_systemone_payload,
    evaluate,
)
from jev_master.key import load_api_key

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
ALLOWED_APPS = ("ticket", "gate", "pitch", "mixed")
ENDPOINT_LABEL = "POST /v1/systemone"

QuestionsFn = Callable[[], dict[str, dict[str, Any]]]
ComposerFn = Callable[[dict[str, Any]], dict[str, Any]]

APP_SPECS: dict[str, tuple[QuestionsFn, ComposerFn, str]] = {
    "ticket": (mixed_ticket_questions, compose_ticket_route, "intent-routing"),
    "mixed": (mixed_ticket_questions, compose_ticket_route, "intent-routing"),
    "gate": (gate_questions, compose_confidence_gate, "confidence-gated-routing"),
    "pitch": (pitch_questions, compose_pitch_score, "composite-scoring"),
}


def resolve_static_dir() -> Path:
    here = Path(__file__).resolve()
    candidates = [
        here.parents[3] / "apps" / "jev_browser" / "static",
        Path.cwd() / "apps" / "jev_browser" / "static",
    ]
    for path in candidates:
        if (path / "index.html").is_file():
            return path
    raise FileNotFoundError(
        "JevBrowser static files not found (expected apps/jev_browser/static/index.html)"
    )


def playground_payload(state: str, app: str = "mixed") -> dict[str, Any]:
    """Shipped System One payload for an app. Mixed uses mixed_ticket_questions()."""
    questions_fn, _, _ = _spec(app)
    return build_systemone_payload(state, questions_fn())


def run_playground(
    state: str,
    app: str = "mixed",
    *,
    api_key: str,
    transport: Transport | None = None,
) -> dict[str, Any]:
    questions_fn, composer, pattern = _spec(app)
    questions = questions_fn()
    result = evaluate(state, questions, api_key=api_key, transport=transport)
    decision = composer(result.answers)
    if not isinstance(decision, dict) or not decision:
        raise ValueError("composer returned an empty decision")
    return {
        "app": app,
        "pattern": pattern,
        "model": result.model,
        "endpoint": ENDPOINT_LABEL,
        "state": state,
        "questions": questions,
        "answers": answers_as_json(result.answers),
        "decision": decision,
        "usage": result.usage,
    }


def evaluate_body(
    body: dict[str, Any],
    *,
    api_key: str,
    transport: Transport | None = None,
) -> dict[str, Any]:
    if not isinstance(body, dict):
        raise ValueError("request body must be a JSON object")
    state = body.get("state")
    if not isinstance(state, str) or not state.strip():
        raise ValueError("state must be a non-empty string")
    app = body.get("app") or "mixed"
    if not isinstance(app, str):
        raise ValueError(f"app must be one of {', '.join(ALLOWED_APPS)}")
    return run_playground(state.strip(), app, api_key=api_key, transport=transport)


def _spec(app: str) -> tuple[QuestionsFn, ComposerFn, str]:
    try:
        return APP_SPECS[app]
    except KeyError as exc:
        raise ValueError(f"app must be one of {', '.join(ALLOWED_APPS)}") from exc


class PlaygroundHandler(BaseHTTPRequestHandler):
    server_version = "JevBrowser/0.1"

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        target = self._safe_static(path)
        if target is None:
            body = b"not found"
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self._send_file(target)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path != "/api/evaluate":
            self._send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        try:
            body = json.loads(raw.decode("utf-8") or "null")
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"error": "invalid JSON"})
            return
        try:
            api_key = self.server.key_loader()
        except RuntimeError as exc:
            self._send_json(503, {"error": str(exc)})
            return
        try:
            payload = evaluate_body(body, api_key=api_key, transport=self.server.transport)
        except ValueError as exc:
            self._send_json(400, {"error": str(exc)})
            return
        except SystemOneError as exc:
            self._send_json(502, {"error": str(exc), "status": exc.status})
            return
        except Exception as exc:
            self._send_json(500, {"error": f"{type(exc).__name__}: {exc}"})
            return
        self._send_json(200, payload)

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("jev-browser %s - %s\n" % (self.address_string(), fmt % args))

    def _safe_static(self, url_path: str) -> Path | None:
        if url_path == "/":
            url_path = "/index.html"
        rel = unquote(url_path).lstrip("/")
        if not rel or ".." in Path(rel).parts:
            return None
        root = Path(self.server.static_dir).resolve()
        target = (root / rel).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            return None
        return target

    def _send_file(self, path: Path) -> None:
        data = path.read_bytes()
        ctype = {
            ".html": "text/html; charset=utf-8",
            ".js": "text/javascript; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".svg": "image/svg+xml",
            ".json": "application/json; charset=utf-8",
        }.get(path.suffix.lower()) or (mimetypes.guess_type(path.name)[0] or "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)


class PlaygroundServer(ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(
        self,
        server_address: tuple[str, int],
        RequestHandlerClass: type[BaseHTTPRequestHandler] = PlaygroundHandler,
        *,
        static_dir: Path,
        transport: Transport | None = None,
        key_loader: Callable[[], str] | None = None,
    ) -> None:
        self.static_dir = static_dir
        self.transport = transport
        self.key_loader = key_loader or load_api_key
        super().__init__(server_address, RequestHandlerClass)


def make_server(
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    *,
    static_dir: Path | None = None,
    transport: Transport | None = None,
    key_loader: Callable[[], str] | None = None,
) -> PlaygroundServer:
    return PlaygroundServer(
        (host, port),
        PlaygroundHandler,
        static_dir=static_dir if static_dir is not None else resolve_static_dir(),
        transport=transport,
        key_loader=key_loader,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="JevBrowser local playground")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="bind port (default 8765)")
    args = parser.parse_args(argv)
    httpd = make_server(DEFAULT_HOST, args.port)
    url = f"http://{DEFAULT_HOST}:{args.port}"
    print(f"JevBrowser  {url}", flush=True)
    print(f"model {DEFAULT_MODEL}  {ENDPOINT_LABEL}  ({SYSTEMONE_URL})", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped", file=sys.stderr)
        return 0
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

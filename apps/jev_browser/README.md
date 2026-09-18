# JevBrowser

Local playground for typed Jev (System One) decisions. Paste unstructured state, run Choice + Score + Noul together, and inspect the **composed decision in code** — department + escalate-or-act, a confidence gate, or a weighted pitch score.

This is a decision inspector, not a chatbot and not a browser-use agent. Inspired by the [TypeSafe playground](https://console.typesafe.ai/playground), [docs](https://docs.typesafe.ai/introduction), and the [smart-home demo](https://docs.typesafe.ai/demos/smart-home) (cite only; not a vendor clone).

## Launch

```bash
python -m jev_master.apps.jev_browser
```

Then open http://127.0.0.1:8765

Also: `python -m jev_master browser`, `jev-browser`, or `python apps/jev_browser`. Bind is `127.0.0.1:8765`; pass `--port` to change it.

The page never sees an API key. The server calls `load_api_key()` only when you click Run (`TYPESAFE_API_KEY` or the key file outside this repo).

## API

`POST /api/evaluate` with `{ "state": "...", "app": "ticket"|"gate"|"pitch"|"mixed" }`.

Mixed (default) uses `ticket_router.mixed_ticket_questions()` — Choice + Score + Noul in one `POST /v1/systemone` call with `model: jev-latest`. The JSON response is `{ answers, decision }`; the decision is always a structured object from the shipped composers, never raw prose.

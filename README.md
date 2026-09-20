<p align="center">
  <img src="docs/assets/live-run.png" alt="Live Jev run: POST /v1/systemone with Choice + Score + Noul" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/model-jev--latest-14b8a6" alt="jev-latest">
  <img src="https://img.shields.io/badge/POST-/v1/systemone-0f766e" alt="System One">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-5eead4" alt="MIT">
  <img src="https://img.shields.io/badge/catalog-382_citations-134e4a" alt="382 citations">
</p>

<p align="center"><b>State in. Typed answers out. Your code decides.</b></p>

# jev-master

A small Python monorepo for [TypeSafe Jev](https://docs.typesafe.ai/concepts/system-one): live compose apps, a `POST /v1/systemone` client, and a cited map of the public field.

Jev is not a chatbot. You send a **state** (the thing to judge) and named **questions**. It returns probabilities your program can branch on. This repo never parses generated prose.

The screenshot is a real `jev-1.13.0` call on `examples/stripe-ticket.txt`: department `billing` (0.69), frustration `1.0`, urgency `0.99` → `act` / `billing_priority_queue`. Raw JSON: [`docs/assets/live-run.json`](docs/assets/live-run.json).

## Contents

- [What this is](#what-this-is)
- [What Jev returns](#what-jev-returns)
- [Quickstart](#quickstart)
- [Which app to run](#which-app-to-run)
- [Example output](#example-output)
- [Browser playground](#browser-playground)
- [Images (TypeSafe Jev cannot see pixels)](#images-typesafe-jev-cannot-see-pixels)
- [Field map](#field-map)
- [Secrets](#secrets)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## What this is

| Layer | Role |
| --- | --- |
| **This repo** | Runnable composers + tests + catalog |
| **TypeSafe Jev** | Hosted text decision model (`api.typesafe.ai`) |
| **Djev** | Separate Maisa preview with **native images** ([djev.dev](https://djev.dev)) — not TypeSafe |
| **awesome-jev lists** | URL directories only |

Not affiliated with TypeSafe. Vendor latency/price numbers are theirs.

## What Jev returns

One HTTP call can mix all three:

| Primitive | Ask | You get |
| --- | --- | --- |
| **Choice** | Which option? | `choice`, `probabilities`, `confidence` |
| **Score** | Where on this rubric? | `score`, `legend`, `probabilities`, `confidence` |
| **Noul** | Is this true? | `noul` in `[0, 1]` |

```
state + questions  →  POST https://api.typesafe.ai/v1/systemone
                      typed answers (no prose)
                   →  compose_*() in this repo
                   →  route / gate / score
```

Change a coefficient in Python when policy changes. Do not rewrite a prompt.

## Quickstart

**Need:** Python 3.10+, a TypeSafe key from [console.typesafe.ai/settings/keys](https://console.typesafe.ai/settings/keys).

Never commit the key. Export it, or keep it outside the repo (this tree gitignores `.env` and `jevkey.txt`).

```bash
git clone https://github.com/kevin9327/jev-master
cd jev-master
python -m pip install -e ".[dev]"
python -m pytest
```

Set `TYPESAFE_API_KEY` in the current shell (PowerShell: `$env:TYPESAFE_API_KEY = '…'` · bash: `export` that same name), then:

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt
```

You should see JSON with `answers` (from Jev) and `decision` (from this repo).

## Which app to run

| Command | When to use it | Composed result |
| --- | --- | --- |
| `python -m jev_master ticket --state examples/stripe-ticket.txt` | Support / queue routing | department + `act`/`escalate` + handler |
| `python -m jev_master gate --state examples/voice-command.txt` | Risky action, need a confidence bar | `act` / `confirm` / `escalate` |
| `python -m jev_master pitch --state examples/pitch.txt` | Weighted score, not one label | 0–1 score + verdict |
| `python -m jev_master bot --state examples/stripe-ticket.txt` | Canned replies, not a chat LLM | `reply` / `escalate` / `block` |
| `python -m jev_master harness --state examples/rm-step.json` | Agent wants to run a tool | `execute` / `confirm` / `reject` |
| `python -m jev_master code --state examples/risky.diff` | Diff merge gate | `merge` / `comment` / `block` |
| `python -m jev_master browser` | Inspect probabilities in a UI | same composers, port **8765** |
| `python -m jev_master catalog` | Browse 382 cited projects | links only, nothing cloned |
| `python -m jev_master catalog --kind vision` | Image-related citations | Djev, OCR-then-Jev, local VL |

Standalone packages of the same ideas: [jev-bot](https://github.com/kevin9327/jev-bot) · [jev-harness](https://github.com/kevin9327/jev-harness) · [jev-code](https://github.com/kevin9327/jev-code)

Each app folder has a short README: [`apps/ticket_router`](apps/ticket_router), [`apps/confidence_gate`](apps/confidence_gate), [`apps/pitch_score`](apps/pitch_score), [`apps/jev_bot`](apps/jev_bot), [`apps/jev_harness`](apps/jev_harness), [`apps/jev_code`](apps/jev_code), [`apps/jev_browser`](apps/jev_browser).

## Example output

Ticket sample (`examples/stripe-ticket.txt`):

```text
Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.
```

Live capture (abridged):

```json
{
  "answers": {
    "department": { "choice": "billing", "confidence": 0.53 },
    "frustration": { "score": 1.0 },
    "is_urgent": { "noul": 0.99 }
  },
  "decision": {
    "department": "billing",
    "action": "act",
    "handler": "billing_priority_queue"
  }
}
```

`answers` come from Jev. `decision` is composed here. Tests inject the same answer shape without hitting the network (`jev_master.client` vs `compose_*()`).

## Browser playground

```bash
python -m jev_master browser
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765). The page calls the same composers. The API key stays on the server process, not in the browser bundle.

## Images (TypeSafe Jev cannot see pixels)

Official TypeSafe docs: **text / JSON only**. On X, TypeSafe staff said [wait a while](https://x.com/dotpem/status/2101335033609138382).

How the field still “judges images” (cited, **not** vendored into this tree):

| Method | What reaches the decision model | Examples |
| --- | --- | --- |
| OCR / caption | Text | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) · [nothotdog](https://github.com/anishsrinivasan/nothotdog) |
| CV → JSON | Scene numbers | [jev-drone](https://github.com/RomanSlack/jev-drone) |
| Swap the model | Pixels | [djev-dev](https://github.com/Davipar/djev-dev) · [jev_local](https://github.com/Argos1111/jev_local) · [jev-visual](https://github.com/hr98w/jev-visual) |
| Pixel questions | A text grid (drawing, not seeing) | [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) |

[Djev](https://djev.dev) is a **Maisa** invite-only preview. Your `TYPESAFE_API_KEY` does not work there.

```bash
python -m jev_master catalog --kind vision
```

## Field map

382 GitHub/X citations, 2026-09-20. **Links only** — this repo does not clone or submodule them.

```bash
python -m jev_master catalog                 # all
python -m jev_master catalog --kind browser  # computer use
python -m jev_master catalog --kind vision   # images
python -m jev_master catalog --json          # machine-readable
```

Kinds: `official` `sdk` `agent` `browser` `vision` `app` `game` `research` `list` `x`

- Table: [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md)
- JSON: [`docs/ecosystem.json`](docs/ecosystem.json)

Headline citations: [python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) · [JS SDK](https://github.com/typesafe-ai/typesafe-sdk-js) · [skills](https://github.com/typesafe-ai/skills) · [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [djev-dev](https://github.com/Davipar/djev-dev) · [awesome-jev](https://github.com/cobanov/awesome-jev)

TypeSafe: [intro](https://docs.typesafe.ai/introduction) · [API](https://docs.typesafe.ai/api) · [patterns](https://docs.typesafe.ai/patterns)

## Secrets

Runtime-only. Do not paste keys into README, tests, issues, or screenshots.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `TYPESAFE_API_KEY is not set` | Export the env var in **this** shell, then rerun |
| HTTP 401 | Wrong product: TypeSafe key → `api.typesafe.ai`. Djev needs a `djev_invite_…` code |
| HTTP 403 / waitlist | Key exists but the TypeSafe account is not enabled yet |
| `pip install -e .` fails on Windows | Use Python 3.10+; tests still run with `PYTHONPATH=src` (`python -m pytest`) |
| Browser page empty | Start `python -m jev_master browser` first, then open port 8765 |
| Want a catalog kind | `--kind` must be one of the kinds listed above |

## License

MIT. See [LICENSE](LICENSE).

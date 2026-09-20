<p align="center">
  <img src="docs/assets/live-run.png" alt="Live Jev run: POST /v1/systemone with Choice + Score + Noul" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/model-jev--latest-14b8a6" alt="jev-latest">
  <img src="https://img.shields.io/badge/POST-/v1/systemone-0f766e" alt="System One endpoint">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-5eead4" alt="MIT">
  <img src="https://img.shields.io/badge/catalog-382_citations-134e4a" alt="382 catalog citations">
</p>

<p align="center"><b>State in. Typed answers out. Your code decides.</b></p>

# jev-master

Runnable compose apps for [TypeSafe Jev](https://docs.typesafe.ai/concepts/system-one), plus a cited map of the rest of the field.

Jev is not a chatbot. You send a *state* and typed *questions*; it returns Choice / Score / Noul probabilities. This repo keeps control flow in Python.

The screenshot is a real `jev-1.13.0` call on `examples/stripe-ticket.txt`: department `billing` (0.69), frustration `1.0`, urgency `0.99` → `act` / `billing_priority_queue`. Raw JSON: [`docs/assets/live-run.json`](docs/assets/live-run.json).

## What you get

1. **Apps you can run** — ticket router, confidence gate, pitch score, bot, harness, merge gate, browser playground.
2. **A live client** — `POST https://api.typesafe.ai/v1/systemone`, mixed primitives in one request.
3. **A field map** — 382 GitHub/X citations in [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md). Links only; nothing is cloned.

Not affiliated with TypeSafe. Djev ([djev.dev](https://djev.dev)) is a separate Maisa preview with native images.

## Quickstart

Python 3.10+. Key from [console.typesafe.ai/settings/keys](https://console.typesafe.ai/settings/keys) as `TYPESAFE_API_KEY` (never commit it).

```bash
git clone https://github.com/kevin9327/jev-master
cd jev-master
python -m pip install -e ".[dev]"
python -m pytest
python -m jev_master ticket --state examples/stripe-ticket.txt
```

That command prints typed `answers` plus a composed `decision`. Same shape if you run it twice.

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt   # which queue, escalate?
python -m jev_master gate --state examples/voice-command.txt     # act / confirm / escalate
python -m jev_master pitch --state examples/pitch.txt            # weighted 0–1 score
python -m jev_master bot --state examples/stripe-ticket.txt      # canned reply / block
python -m jev_master harness --state examples/rm-step.json       # execute / reject a tool
python -m jev_master code --state examples/risky.diff            # merge / comment / block
python -m jev_master browser                                     # playground on :8765
python -m jev_master catalog --kind vision                       # cited field map
```

## Apps

| App | Pattern | Code composes |
| --- | --- | --- |
| [`apps/ticket_router`](apps/ticket_router) | [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) | department + escalate-or-act |
| [`apps/confidence_gate`](apps/confidence_gate) | [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) | act / confirm / escalate |
| [`apps/pitch_score`](apps/pitch_score) | [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) | weighted 0–1 + verdict |
| [`apps/jev_bot`](apps/jev_bot) | Support bot (not an LLM) | `reply` / `escalate` / `block` |
| [`apps/jev_harness`](apps/jev_harness) | Tool-call harness | `execute` / `confirm` / `reject` |
| [`apps/jev_code`](apps/jev_code) | Diff merge gate | `merge` / `comment` / `block` |
| [`apps/jev_browser`](apps/jev_browser) | Local playground | same composers, live bars |

Standalone packages: [jev-bot](https://github.com/kevin9327/jev-bot) · [jev-harness](https://github.com/kevin9327/jev-harness) · [jev-code](https://github.com/kevin9327/jev-code)

Change a coefficient in Python when policy changes. Do not rewrite a prompt.

## How a call works

```
state + questions  →  POST /v1/systemone (jev-latest)
                      typed answers (no prose)
                   →  compose_*() here
                   →  route / gate / score
```

| Primitive | Returns |
| --- | --- |
| **Choice** | `choice`, `probabilities`, `confidence` |
| **Score** | `score`, `legend`, `probabilities`, `confidence` |
| **Noul** | `noul` in `[0, 1]` |

The HTTP client (`jev_master.client`) is separate from composers, so tests inject real-shaped answers without the network.

Example state (`examples/stripe-ticket.txt`):

```text
Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.
```

## Images

**TypeSafe Jev is text-only.** Official reply on X: [wait a while](https://x.com/dotpem/status/2101335033609138382). People still “judge images” by one of these (cited, not vendored):

| Method | What reaches Jev | Repos |
| --- | --- | --- |
| OCR / caption | Text | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) · [nothotdog](https://github.com/anishsrinivasan/nothotdog) |
| CV → JSON | Scene numbers | [jev-drone](https://github.com/RomanSlack/jev-drone) |
| Swap the model | Pixels | [djev-dev](https://github.com/Davipar/djev-dev) · [jev_local](https://github.com/Argos1111/jev_local) · [jev-visual](https://github.com/hr98w/jev-visual) |
| Pixel questions | A text grid (drawing, not seeing) | [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) |

Djev is **not** TypeSafe. It is a Maisa research preview with native vision and invite-only keys.

```bash
python -m jev_master catalog --kind vision
```

## Field map

awesome-jev lists are URL directories. This repo ships the runnable layer and indexes the rest.

```bash
python -m jev_master catalog
python -m jev_master catalog --kind browser
```

Full table: [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md) · JSON: [`docs/ecosystem.json`](docs/ecosystem.json) · 382 entries, 2026-09-20.

Headline citations:

- Official — [python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) · [JS SDK](https://github.com/typesafe-ai/typesafe-sdk-js) · [skills](https://github.com/typesafe-ai/skills)
- Agents — [foreman](https://github.com/thruwire/foreman) · [winnow](https://github.com/GhalebDweikat/winnow)
- Browser — [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
- Vision — [djev-dev](https://github.com/Davipar/djev-dev) · [djev-spark](https://github.com/mmastrac/djev-spark) · [PlayJev](https://github.com/OmniJev/PlayJev)
- Lists — [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) · [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev)

TypeSafe docs: [intro](https://docs.typesafe.ai/introduction) · [API](https://docs.typesafe.ai/api) · [patterns](https://docs.typesafe.ai/patterns)

## Secrets

Runtime-only. `.env`, `jevkey.txt`, and TypeSafe key files are gitignored. Do not paste keys into README, tests, or screenshots.

## License

MIT. See [LICENSE](LICENSE).

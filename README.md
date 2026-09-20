<p align="center">
  <img src="docs/assets/live-run.png" alt="Live Jev run: POST /v1/systemone with Choice + Score + Noul, composed into department + escalate-or-act" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/model-jev--latest-14b8a6" alt="jev-latest">
  <img src="https://img.shields.io/badge/POST-api.typesafe.ai%2Fv1%2Fsystemone-0f766e" alt="System One endpoint">
  <img src="https://img.shields.io/badge/primitives-Choice%20%2B%20Score%20%2B%20Noul-134e4a" alt="primitives">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-5eead4" alt="MIT">
  <img src="https://img.shields.io/badge/not-DocAgent-1f2937" alt="Not DocAgent">
  <img src="https://img.shields.io/badge/not-an%20LLM%20chat-111827" alt="Not an LLM chat">
</p>

<p align="center"><b>State in. Typed answers out. Your code decides.</b><br>
<code>POST /v1/systemone</code> · <code>jev-latest</code> · Choice + Score + Noul in one call · compose the route in Python.</p>

# jev-master

Jev is TypeSafe's first [System One](https://docs.typesafe.ai/concepts/system-one) model: send a *state* and typed *questions*, get structured *answers* your program can branch on. This repo is a GitHub-ready monorepo of small apps that **keep control flow in code** and treat Jev as a frontier-intelligence function call — not a chatbot, not a document converter.

The screenshot above is a **real** `jev-latest` (`jev-1.13.0`) evaluation of the docs ticket sample (`examples/stripe-ticket.txt`), not a mock SVG. Live capture: Choice `billing` (p=0.69, confidence 0.53), Score frustration `1.0` (civil), Noul urgency `0.99` → composed `act` / `billing_priority_queue`. Raw JSON: [`docs/assets/live-run.json`](docs/assets/live-run.json).

## Why this exists

Large language models generate text. When software needs a judgment — *which queue?* *act or escalate?* *what is the weighted score?* — parsing a paragraph is the wrong interface. Jev returns:

| Question | Returns |
| --- | --- |
| **Choice** | `choice`, `probabilities` (sum ~1), `confidence` |
| **Score** | `score`, `legend`, `probabilities`, `confidence` |
| **Noul** | `noul` in `[0, 1]` |

All three mix in a **single** `POST https://api.typesafe.ai/v1/systemone`. Code composes the application decision.

## Quickstart

Python 3.10+. Get a TypeSafe key from the [dashboard](https://console.typesafe.ai/settings/keys) and export it as `TYPESAFE_API_KEY` (never commit it).

```bash
git clone https://github.com/kevin9327/jev-master
cd jev-master
python -m pip install -e ".[dev]"
python -m pytest
python -m jev_master ticket --state examples/stripe-ticket.txt
```

The north-star command prints JSON with typed `answers` plus a composed `decision` (`department` + `escalate`/`act` + handler). Run it twice on the same state: the fields stay structured and match the live answers.

Independently launchable sub-projects:

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt   # intent routing
python -m jev_master gate --state examples/voice-command.txt     # confidence gate
python -m jev_master pitch --state examples/pitch.txt            # composite score
python -m jev_master browser                                     # JevBrowser on :8765
python -m jev_master catalog                                     # cited field map (not clones)
python -m jev_master bot --state examples/stripe-ticket.txt      # JevBot canned replies
python -m jev_master harness --state examples/rm-step.json       # JevHarness tool gate
python -m jev_master code --state examples/risky.diff            # JevCode merge gate
```

Or from the app folders:

```bash
python -m apps.ticket_router --state examples/stripe-ticket.txt
python -m apps.confidence_gate --state examples/voice-command.txt
python -m apps.pitch_score --state examples/pitch.txt
python -m apps.jev_bot --state examples/stripe-ticket.txt
python -m apps.jev_harness --state examples/rm-step.json
python -m apps.jev_code --state examples/risky.diff
python -m apps.jev_browser
```

## Sub-projects

| App | TypeSafe pattern | What code composes |
| --- | --- | --- |
| [`apps/ticket_router`](apps/ticket_router) | [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) | department + escalate-or-act |
| [`apps/confidence_gate`](apps/confidence_gate) | [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) | act / confirm / escalate |
| [`apps/pitch_score`](apps/pitch_score) | [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) | weighted 0–1 score + verdict |
| [`apps/jev_browser`](apps/jev_browser) | Playground in the browser | inspect probabilities + the same composers |
| [`apps/jev_bot`](apps/jev_bot) | Support bot (not a chat LLM) | canned `reply` / `escalate` / `block` |
| [`apps/jev_harness`](apps/jev_harness) | Agent tool-call harness | `execute` / `confirm` / `reject` |
| [`apps/jev_code`](apps/jev_code) | Diff merge gate | `merge` / `comment` / `block` |

Sibling GitHub repos (same ideas, standalone packages):
[jev-bot](https://github.com/kevin9327/jev-bot) · [jev-harness](https://github.com/kevin9327/jev-harness) · [jev-code](https://github.com/kevin9327/jev-code)

Atomic questions, then weights and thresholds in Python. If priorities change, change a coefficient — do not rewrite a prompt.

## Architecture

```
state + questions  -->  POST /v1/systemone (jev-latest)
                       typed answers (no prose)
                       -->  compose_*() in this repo
                       -->  route / gate / score
```

The HTTP client (`jev_master.client.build_systemone_payload` / `evaluate`) is separate from the composers so tests feed real-shaped answers without hitting the network.

## Example input

`examples/stripe-ticket.txt` (the [quickstart](https://docs.typesafe.ai/introduction/quickstart) sample):

```text
Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.
```

One mixed request asks department (Choice), frustration (Score), and urgency (Noul). `compose_ticket_route` turns those into a queue name and whether to escalate.

## Secrets

The API key is runtime-only. This tree gitignores `.env`, `jevkey.txt`, and TypeSafe key files. Do not paste keys into README, tests, or screenshots.

## Field map (GitHub + X, cited not cloned)

awesome-jev lists are link directories. **jev-master ships the runnable compose layer** (live `POST /v1/systemone`, mixed Choice+Score+Noul, tests, JevBrowser) and **indexes the rest of the field** without vendoring it. Star rank is not a claim.

| What they are | What this repo is |
| --- | --- |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) — curated links | Live client + composers you can run |
| [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) — 400+ directory | Pattern-tagged index in [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md) |
| [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) — use-case notes | Intent routing / confidence gate / composite score as launchable apps |

Surveyed from those lists plus official SDKs, Djev/Maisa vision work, and X (`@typesafeai`, `@davipar`, `@mmastrac`, Browser Use ultrafast). Full JSON: [`docs/ecosystem.json`](docs/ecosystem.json). Print it:

```bash
python -m jev_master catalog
python -m jev_master catalog --kind browser
python -m jev_master catalog --kind vision
```

**TypeSafe Jev does not take images.** On X the official answer is [wait a while](https://x.com/dotpem/status/2101335033609138382). Field workarounds, cited not cloned:

| How | What Jev actually sees | Examples |
| --- | --- | --- |
| OCR / caption | Text | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) · [nothotdog](https://github.com/anishsrinivasan/nothotdog) |
| CV → JSON | Structured scene | [jev-drone](https://github.com/RomanSlack/jev-drone) |
| Swap the model | Pixels | [djev-dev](https://github.com/Davipar/djev-dev) · [jev_local](https://github.com/Argos1111/jev_local) · [jev-visual](https://github.com/hr98w/jev-visual) |
| Pixel questions | Text grid (drawing, not seeing) | [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) |

Djev ([djev.dev](https://djev.dev)) is **Maisa**, not TypeSafe. Invite-only native vision.

Headline citations (not copied into this tree):

- Official: [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) · [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) · [skills](https://github.com/typesafe-ai/skills)
- Agents: [foreman](https://github.com/thruwire/foreman) · [winnow](https://github.com/GhalebDweikat/winnow) · [hermes-jev](https://github.com/keeltrace/hermes-jev)
- Browser: [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
- Vision: [djev-dev](https://github.com/Davipar/djev-dev) · [djev-spark](https://github.com/mmastrac/djev-spark) · [PlayJev](https://github.com/OmniJev/PlayJev)
- Apps: [neo4jev](https://github.com/jexp/neo4jev) · [jev-trader](https://github.com/jarrodwatts/jev-trader) · [classifier-dev](https://github.com/mrmps/classifier-dev)
- Research: [SemIf](https://github.com/TheoLeeCJ/SemIf) · [jevlike](https://github.com/vinnylarouge/jevlike)

Docs: [Introduction](https://docs.typesafe.ai/introduction) · [API](https://docs.typesafe.ai/api) · [Patterns](https://docs.typesafe.ai/patterns)

Not affiliated with TypeSafe. Vendor eval numbers are theirs; this repo ships composition code you can run.

## License

MIT. See [LICENSE](LICENSE).

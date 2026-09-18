# Jev field map (cited, not cloned)

This file is an index of public Jev / TypeSafe System One work.
**We do not vendor, mirror, or submodule these repositories.**
Star counts and trending rank are not claimed.

Surveyed GitHub awesome-jev lists, official TypeSafe repos, and X posts about Jev/System One · 88 cited entries · 2026-09-18.

Sources we read (still not copied into this tree):

- https://github.com/cobanov/awesome-jev
- https://github.com/hellogumbo/awesome-jev
- https://github.com/aliaihub/awesome-jev-usecases
- https://github.com/AbdelStark/awesome-typesafe
- https://github.com/Anil-matcha/awesome-jev-by-typesafe
- https://github.com/typesafe-ai/typesafe-sdk-python
- https://docs.typesafe.ai/introduction
- https://x.com/typesafeai

Method: public GitHub READMEs + X posts. Inclusion is not TypeSafe affiliation.

## Official

- [TypeSafe docs](https://docs.typesafe.ai/introduction) `catalog` — Jev intro, primitives, POST /v1/systemone
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) `client` — Official Python SDK
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) `client` — Official TypeScript/JS SDK
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) `client` — LLM adapter for comparison
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) `other` — Official agent skill
- [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) `catalog` — System One + Jev announcement

## SDKs and clients

- [jevclient](https://github.com/AboveColin/jevclient) `client` — Async Python client
- [jevgo](https://github.com/fgn/jevgo) `client` — Go client + optional Langfuse
- [jev-go](https://github.com/Gaurav-Gosain/jev-go) `client` — Go System One client
- [typesafe-go](https://github.com/zhirschtritt/typesafe-go) `client` — Idiomatic Go SDK
- [typesafe-rs](https://github.com/AbdelStark/typesafe-rs) `client` — Latency-first Rust SDK
- [s1-rs](https://github.com/AbdelStark/s1-rs) `client` — Typed System One layer for Rust
- [typesafe_ai (Elixir)](https://github.com/typesend/typesafe_ai) `client` — Typed Elixir client, offline stubs
- [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) `client` — .NET SDK
- [typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php) `client` — Unofficial PHP SDK
- [typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift) `client` — Swift SDK
- [advocaat](https://github.com/pithings/advocaat) `client` — Dataset questions client
- [zod-jev](https://github.com/jomatsu/zod-jev) `other` — Zod shape + Jev meaning
- [jev-axi](https://github.com/shiftynick/jev-axi) `other` — Shell pick/rate/check/rank/guard
- [semdecide](https://github.com/sharziki/semdecide) `other` — Unix pipeline semantic decisions
- [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) `client` — Laravel typed responses + fakes

## Agents, gates, MCP

- [jev-harness](https://github.com/kevin9327/jev-harness) `confidence-gate` — Tool-call execute/confirm/reject gate
- [jev-code](https://github.com/kevin9327/jev-code) `confidence-gate` — Diff merge/comment/block gate
- [foreman](https://github.com/thruwire/foreman) `confidence-gate` — Supervisor keeps coding agents on task · [X](https://x.com/JoshARosen/status/2100573432089866717)
- [jev-review](https://github.com/devagrawal09/jev-review) `intent-routing` — Staged code-review workflow
- [winnow](https://github.com/GhalebDweikat/winnow) `confidence-gate` — Judge tool results before context
- [jev-guard](https://github.com/leepokai/jev-guard) `confidence-gate` — Allow/ask/deny tool-call risk
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) `intent-routing` — Per-turn Codex model routing
- [pi-jev](https://github.com/y0usaf/pi-jev) `confidence-gate` — Pi agent tool-call gate
- [skillranker](https://github.com/Dicklesworthstone/skillranker) `composite-score` — Rank skills vs session context
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) `client` — MCP connector for Jev
- [jev-mcp](https://github.com/blakestone-x/jev-mcp) `client` — classify/score/check/match/screen
- [hermes-jev](https://github.com/keeltrace/hermes-jev) `confidence-gate` — Hermes decide/rank/verify/assess
- [diffjury](https://github.com/raihankhan-rk/diffjury) `intent-routing` — PR risk router + review coach
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) `other` — Question-design skill for agents
- [bicameral](https://github.com/AbdelStark/bicameral) `other` — System 2 writes, Jev reflexes
- [JevLint](https://github.com/huntedman/JevLint) `other` — Semantic lint via Noul

## Browser and computer use

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) `intent-routing` — Jev picks op+DOM; LLM types only · [X](https://x.com/gregpr07/status/2100411066966749359)
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) `intent-routing` — macOS OCR + bounded Jev actions · [X](https://x.com/awlevin/status/2100262612428894676)
- [aside-jev](https://github.com/himomohi/aside-jev) `confidence-gate` — Aside runtime, Jev decides
- [mobile-jev](https://github.com/droidrun/mobile-jev) `intent-routing` — Android agent, Jev every decision
- [jev-browser (jkudish)](https://github.com/jkudish/jev-browser) `intent-routing` — browser-use experiment
- [JevTest](https://github.com/CorieW/JevTest) `other` — Bounded exploratory browser tests
- [unclutter](https://github.com/kitze/unclutter) `other` — Page clutter removal extension · [X](https://x.com/thekitze/status/2100595129874817340)
- [sift](https://github.com/tylergibbs1/sift) `composite-score` — Re-rank Google results with Jev

## Applications

- [jev-master](https://github.com/kevin9327/jev-master) `catalog` — This monorepo: live compose apps + field map
- [jev-bot](https://github.com/kevin9327/jev-bot) `intent-routing` — Canned-reply support bot, not a chatbot
- [neo4jev](https://github.com/jexp/neo4jev) `fan-out` — Graph hop Choice + Noul per step · [X](https://x.com/0xLogicrw/status/2100478725393686556)
- [jev-trader](https://github.com/jarrodwatts/jev-trader) `intent-routing` — One trade decision per Monad block · [X](https://x.com/jarrodwatts/status/2100356151468585346)
- [HA-Jev](https://github.com/AboveColin/HA-Jev) `other` — Home Assistant entities from Jev
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) `intent-routing` — Route Hono requests by meaning
- [jevlogs](https://github.com/reachjalil/jevlogs) `composite-score` — OTel log triage before LLM
- [pg-jev](https://github.com/realZachi/pg-jev) `other` — PostgreSQL semantic questions
- [killmyidea](https://github.com/monteduro/killmyidea) `intent-routing` — Kill / fix / ship a startup idea
- [jevmeter](https://github.com/ChetasLua/jevmeter) `composite-score` — Score every sentence in a video · [X](https://x.com/chetaslua/status/2100602714204049588)
- [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) `confidence-gate` — Does the paper support the cite?
- [Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) `fan-out` — Discord phishing/spam parallel eval
- [commit-miner](https://github.com/devanshbatham/commit-miner) `intent-routing` — Classify commit diffs
- [jevegis](https://github.com/0xArx/jevegis) `confidence-gate` — LLM app guardrails in one call
- [pkg-gate](https://github.com/hemanth/pkg-gate) `confidence-gate` — npm lifecycle script security gate
- [typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow) `intent-routing` — LangGraph email intent Choice

## Games and simulations

- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) `intent-routing` — Mario from structured emulator state
- [typesafe-snake](https://github.com/sorrycc/typesafe-snake) `intent-routing` — One typed decision per tick
- [heist-one](https://github.com/AbdelStark/heist-one) `other` — Jev judges guards; code owns world
- [jev-drone](https://github.com/RomanSlack/jev-drone) `other` — MuJoCo quadrotor tactical Jev
- [tsai-sc](https://github.com/phyous/tsai-sc) `intent-routing` — StarCraft shareware via Jev
- [jev-little-airways](https://github.com/lbotinelly/jev-little-airways) `fan-out` — ATC divert/hold/clearance live
- [jev-chat](https://github.com/adhyaay-karnwal/jev-chat) `other` — Wrong-use study: chat from Choices

## Open replicas and evals

- [openjev (TheoLeeCJ)](https://github.com/TheoLeeCJ/openjev) `other` — Jev-like on a 3090 at home · [X](https://x.com/hhkkmon/status/2100443314957038010)
- [openjev (razorback16)](https://github.com/razorback16/openjev) `client` — Jev-compatible server on DiffusionGemma
- [system-one-gemma](https://github.com/akash-kamat/system-one-gemma) `other` — Open scoring head on Gemma 3 270M
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) `other` — Blind prompt-injection + vuln code · [X](https://x.com/_GauravGosain/status/2100111398277959715)
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) `other` — Calibration, selective risk, latency
- [jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark) `other` — Korean understanding / medical text
- [jevmlx](https://github.com/bnsd55/jevmlx) `other` — Parallel decisions on Apple MLX · [X](https://x.com/beni_il_/status/2100617387116568956)
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) `client` — Jev-compatible endpoint, open models

## Other directories

- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) `catalog` — Source-backed curated list
- [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) `catalog` — Large directory + awesomejev.com
- [awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) `catalog` — Evidence-backed use cases
- [awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) `catalog` — Official + community index
- [awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) `catalog` — Patterns, prompts, starter code
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) `catalog` — Field guide by decision domain
- [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) `catalog` — Directory + X posts

## X threads

- [@typesafeai](https://x.com/typesafeai) `catalog` — Official product/research posts
- [Vercel AI Gateway Jev](https://x.com/typesafeai/status/2100376436272173088) `client` — Hosted typesafe-ai/jev, no waitlist
- [Browser Use ultrafast](https://x.com/gregpr07/status/2100411066966749359) `intent-routing` — Jev picks browser op + element
- [jev-trader on X](https://x.com/jarrodwatts/status/2100356151468585346) `intent-routing` — On-chain Jev trade loop
- [Logicrw field roundup](https://x.com/0xLogicrw/status/2100478725393686556) `catalog` — Roundup of neo4jev, review, MCP, winnow

## What jev-master adds

Link directories stop at the URL. This repo ships a live `POST /v1/systemone` client, mixed Choice+Score+Noul, compose apps (ticket/gate/pitch plus JevBot/JevHarness/JevCode), JevBrowser, and tests on the shipped builders — then points at the rest of the field.


# Jev field map (cited, not cloned)

This file is an index of public Jev / TypeSafe System One work.
**We do not vendor, mirror, or submodule these repositories.**
Star counts and trending rank are not claimed.

Surveyed GitHub awesome-jev lists, GitHub search, official TypeSafe + Djev docs, and X posts (image/vision harvest + 2026-09-20 field sweep) · 382 cited entries · 2026-09-20.

Sources we read (still not copied into this tree):

- https://github.com/cobanov/awesome-jev
- https://github.com/hellogumbo/awesome-jev
- https://github.com/aliaihub/awesome-jev-usecases
- https://github.com/AbdelStark/awesome-typesafe
- https://github.com/Anil-matcha/awesome-jev-by-typesafe
- https://github.com/typesafe-ai/typesafe-sdk-python
- https://docs.typesafe.ai/introduction
- https://x.com/typesafeai
- https://github.com/kevin9327/jev-visual
- https://x.com/CompleteSkeptic/status/2099925682726002904
- https://github.com/githubnext/localjev
- https://djev.dev
- https://github.com/Davipar/djev-dev
- https://github.com/mmastrac/djev-spark
- https://x.com/LukeberryPi/status/2101307264829149210
- https://jevbest.com/

Method: public GitHub READMEs + X posts. Inclusion is not TypeSafe affiliation.

## Official

- [TypeSafe docs](https://docs.typesafe.ai/introduction) `catalog` — Jev intro, primitives, POST /v1/systemone
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) `client` — Official Python SDK
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) `client` — Official TypeScript/JS SDK
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) `client` — LLM adapter for comparison
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) `other` — Official agent skill
- [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) `catalog` — System One + Jev announcement
- [TypeSafe homepage](https://typesafe.ai) `catalog` — Official product site for System One / Jev
- [System One concept](https://docs.typesafe.ai/concepts/system-one) `catalog` — Official System One / Jev concept page
- [Jev models](https://docs.typesafe.ai/models) `catalog` — Official Jev 1.13.0 model card, aliases, pricing
- [Vercel AI Gateway changelog](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) `client` — typesafe-ai/jev via AI SDK evaluate()
- [OpenRouter Jev 1.13](https://openrouter.ai/typesafe/jev-1.13) `client` — Provider listing for typesafe/jev-1.13
- [Cloudflare AI Jev](https://developers.cloudflare.com/ai/models/typesafe/jev) `client` — Provider-maintained typesafe/jev integration

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
- [jev](https://github.com/dannote/jev) `client` — Elixir/OTP client designed around GenServer replies and pattern matching.
- [jev-dsl](https://github.com/inanna-malick/jev-dsl) `client` — Early-alpha Haskell DSL that encodes typed question packets and decodes answers; HTTP transport is left to the caller.
- [jev-mcp](https://github.com/BYK/jev-mcp) `client` — An eval-first MCP server for Jev, that returns typed judgments (noul, choice, score) with probabilities instead of generated text.
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) `client` — Ranks existing zsh history entries for inline completion; accepting a suggestion does not execute it.
- [jev.nvim](https://github.com/valentynkit/jev.nvim) `client` — Neovim plugin that splits the buffer into functions with Treesitter, scores each against a plain-language question with Jev, and ranks answe
- [Jevbridge](https://github.com/gamesonrblx/Jevbridge) `client` — ACP/MCP adapter for using Jev alongside coding and chat models.
- [jevr](https://github.com/simxnherrera/jevr) `client` — Native R client for typed questions and provider-independent answers through TypeSafe or OpenRouter.
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) `client` — Ruby client with standard-library transport for TypeSafe and OpenRouter decision endpoints.
- [typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java) `client` — Community Java 17 client for Choice, Score, and Noul, with an optional Spring Boot starter.
- [typesafe-ai-ruby](https://github.com/hnegishi/typesafe-ai-ruby) `client` — Unofficial Ruby gem for TypeSafe Jev
- [jevis](https://github.com/jaewgwon/jevis) `client` — Flutter integration-test package driven by Jev
- [typesafe-ai-jev (Java)](https://github.com/kcb-swe-gh/typesafe-ai-jev) `client` — Java 21 client for Jev structured decisions
- [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) `client` — Scala 3 / ZIO client for Jev
- [typesafe-sdk (Ruby)](https://github.com/joshmn/typesafe-sdk) `client` — Ruby client for TypeSafe System One
- [swift-typesafe](https://github.com/ainame/swift-typesafe) `client` — Unofficial Swift 6 SDK
- [typesafe_sdk (Elixir)](https://github.com/nshkrdotcom/typesafe_sdk) `client` — Elixir Hex SDK for System One / Jev
- [typesafe-cli (y0usaf)](https://github.com/y0usaf/typesafe-cli) `client` — Shell noul/choice/score CLI
- [jev-java](https://github.com/Olti1947/jev-java) `client` — Java 17 SDK for Jev System One
- [jev-sdk-go](https://github.com/kazz187/jev-sdk-go) `client` — Go client with typed Choice/Score/Noul
- [hs-jev](https://github.com/getmissionctrl/hs-jev) `client` — Haskell System One client
- [jev-cli (Rust)](https://github.com/shaharia-lab/jev-cli) `client` — Rust CLI for TypeSafe Jev
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) `other` — SQLite C extension for Jev judgments
- [jevkit](https://github.com/ariel-frischer/jevkit) `other` — Rust question linter + caller
- [n8n-nodes-jev-systemone](https://github.com/withabdul/n8n-nodes-jev-systemone) `client` — n8n classify/score then IF/Switch
- [typesafe-sdk-ruby (afurm)](https://github.com/afurm/typesafe-sdk-ruby) `client` — Community Ruby TypeSafe client

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
- [agent-router](https://github.com/nidhi-singh02/agent-router) `confidence-gate` — Pre-release Herdr integration that filters eligible coding models by quota and policy before Jev ranks them.
- [blink](https://github.com/ellipsis-dev/blink) `confidence-gate` — Navigates file and directory names with Jev-guided walkers to find codebase paths for a natural-language query.
- [Canny](https://github.com/qkal/Canny) `confidence-gate` — Evidence ledger that challenges unsupported "done" claims from coding agents.
- [is-malicious](https://github.com/luantak/is-malicious) `confidence-gate` — Scans source, configuration, build, and CI files with Jev, then reports suspicious behavior and implicated lines before the code is run.
- [jev-belay](https://github.com/valentynkit/jev-belay) `confidence-gate` — Claude Code Stop hook that checks the transcript for evidence before trusting a "done" claim, spending one four-question Jev call only when
- [jev-commit](https://github.com/valentynkit/jev-commit) `confidence-gate` — Pre-commit hook where one Jev call judges whether the commit message matches the staged diff, flags debug leftovers and unmentioned work, an
- [jev-pref](https://github.com/doeixd/jev-pref) `confidence-gate` — Linter that has Jev check code changes against project preferences from `jev-pref.json` and feeds findings back to coding agents.
- [jev-review MCP plugin](https://github.com/NiazMorshed2007/jev-review) `confidence-gate` — Local-first continuous software-quality review for coding agents.
- [jev-router](https://github.com/gargpratyush/jev-router) `confidence-gate` — Chooses a model for each fresh Claude Code or Codex turn while wrapping the existing CLI.
- [jevwire](https://github.com/Brainwires/jevwire) `confidence-gate` — MCP tools, an embeddable decision library, and advisory or restrictive Claude Code hooks; judgments do not grant native permissions.
- [opencode-jev-orchestrator](https://github.com/aaronshaf/opencode-jev-orchestrator) `confidence-gate` — Keeps an OpenCode parent model fixed and uses Jev difficulty judgments to delegate harder turns to temporary subagents.
- [perch](https://github.com/lakeday-org/perch) `confidence-gate` — Semantic code linter that evaluates code units against configurable Jev questions.
- [pi-warden](https://github.com/DevMortimer/pi-warden) `confidence-gate` — Pi extension that judges rule compliance, risky actions, stuck loops, and completion claims; enforcement depends on the hook and policy.
- [skillbox](https://github.com/kitze/skillbox) `confidence-gate` — Self-hosted skill library with optional Jev relevance recommendations over an authorized catalog.
- [supercov](https://github.com/supercorp-ai/supercov) `confidence-gate` — Scores source files so coding agents can prioritize code-quality work.
- [wakegate](https://github.com/shitianfang/wakegate) `confidence-gate` — Experimental gate where Jev decides whether a timer or incoming event is worth resuming a sleeping agent's LLM; code skips only when Jev is
- [fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) `other` — Codex port that restores Jev-selected verbatim history around native session compaction.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) `other` — Claude Code plugin and library that score tool-call/result pairs for deletion or truncation while retaining selected text verbatim.
- [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) `other` — Pi extension that prunes stale tool history and leaves summary compaction to Pi when pruning is insufficient.
- [pi-jev-compact](https://github.com/ilkerulusoy/pi-jev-compact) `other` — Selective, verbatim context compaction for Pi using Jev model.
- [pi-jev-context](https://github.com/kevinpita/pi-jev-context) `other` — Opt-in Pi extension that filters older messages from model requests while preserving the original session history.
- [yoshi](https://github.com/compozy/yoshi) `other` — Experimental Claude Code/Codex proxy that uses Jev to prune request context while preserving tool-call protocol structure.
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) `confidence-gate` — Pi auto-mode: Jev auto-approves bash/write/edit, fail-closed
- [askjev](https://github.com/pZacca/askjev) `client` — Unofficial MCP server for Jev
- [pi-jev-typesafe](https://github.com/nardinmarcus/pi-jev-typesafe) `client` — Zero-dependency jev_ask tool for Pi with question linting and budget caps
- [jev-model-router](https://github.com/az9713/jev-model-router) `intent-routing` — Jev model router on the Vercel AI Gateway
- [jev-router (gmaxxxie)](https://github.com/gmaxxxie/jev-router) `intent-routing` — Per-prompt Pi model routing driven by Jev
- [skill-router](https://github.com/lomeshdutta/skill-router) `intent-routing` — Jev picks which installed Claude Code skill a session needs
- [foreman (reification-labs)](https://github.com/reification-labs/foreman) `fan-out` — Elixir/Phoenix specialist agents behind a System Two foreman
- [jeffrey](https://github.com/thomasbrueggemann/jeffrey) `intent-routing` — Coding agent CLI: Jev decides next step, LLM does the work
- [ci-gatekeeper-bot-jev](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev) `confidence-gate` — GitHub Action triages PRs with Jev before expensive review
- [jevcumber](https://github.com/RubyBrewsday/jevcumber) `intent-routing` — Cucumber .feature files: Jev resolves Gherkin, Playwright runs
- [jevmap](https://github.com/aegsrl7/jevmap) `other` — Jev hands a coding agent the ten files that matter for a task
- [jev-mcp (codaaiteam)](https://github.com/codaaiteam/jev-mcp) `client` — MCP server: classify, score, check, gate risky tool calls
- [jev-baton](https://github.com/shitianfang/jev-baton) `confidence-gate` — Pass the baton between LLM and Jev: MCP + escalation contract
- [jev-harness-router](https://github.com/JoacoMarc/jev-harness-router) `intent-routing` — Per-turn harness router: model tier, tools, skill, effort budget
- [hermes-jev-north-star](https://github.com/poponline63/hermes-jev-north-star) `confidence-gate` — Hermes skill: Jev ranks what is still unproven
- [the-llm-dispatcher](https://github.com/Rawson08/the-llm-dispatcher) `intent-routing` — OpenAI-compatible proxy: Jev dispatches cheapest sufficient model
- [typesafe-mcp (y0usaf)](https://github.com/y0usaf/typesafe-mcp) `client` — Unofficial MCP evaluate(state, questions)
- [jev-cli (tumf)](https://github.com/tumf/jev-cli) `client` — CLI + stdio MCP + bundled skill
- [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) `client` — MCP tools for TypeSafe Jev judgments
- [jev-compactor](https://github.com/edwardyen724-g/jev-compactor) `other` — Context compaction using System One questions
- [jev-system-architect](https://github.com/samtay32/jev-system-architect) `other` — Skill mapping fuzzy judgment to Choice/Score/Noul
- [jev-rules](https://github.com/EliaAlberti/jev-rules) `intent-routing` — Jev picks which Claude rules apply per prompt
- [jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher) `intent-routing` — Probe MCP tools then Jev picks function/args
- [quackd](https://github.com/rokbenko/quackd) `intent-routing` — Multi-robot harness CLI with Jev discrete steps
- [hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin) `client` — Hermes Agent tools plugin for Jev
- [jev-pruner](https://github.com/tamaratran/jev-pruner) `other` — Claude Code plugin: Jev trims bash output
- [jev-security-scan](https://github.com/win4r/jev-security-scan) `confidence-gate` — TypeSafe Jev review of Skills/MCP
- [JevRouter](https://github.com/BillionsBobby/JevRouter) `intent-routing` — Jev-powered router for models, tools, subagents
- [jev (Claude plugin)](https://github.com/BorisLeMeec/jev) `other` — Claude Code plugin for Jev
- [jev-shield](https://github.com/caiovicentino/jev-shield) `confidence-gate` — MCP semantic firewall
- [vercel-labs/fx](https://github.com/vercel-labs/fx) `confidence-gate` — typesafe_permission_reviewer using Jev
- [jevcache](https://github.com/kushals256/jevcache) `other` — Skip duplicate LLM calls when Jev says same intent
- [jev-s](https://github.com/wuyoscar/jev-s) `other` — Codex/Claude/OpenCode Jev skills bundle
- [agent-xray](https://github.com/morlex01/agent-xray) `other` — Jev analyzes agent traces into a Fix Pack
- [jev-pii-guardrail](https://github.com/jms-dcksn/jev-pii-guardrail) `confidence-gate` — PII detect around LLM calls

## Browser and computer use

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) `intent-routing` — Jev picks op+DOM; LLM types only · [X](https://x.com/gregpr07/status/2100411066966749359)
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) `intent-routing` — macOS OCR + bounded Jev actions · [X](https://x.com/awlevin/status/2100262612428894676)
- [aside-jev](https://github.com/himomohi/aside-jev) `confidence-gate` — Aside runtime, Jev decides
- [mobile-jev](https://github.com/droidrun/mobile-jev) `intent-routing` — Android agent, Jev every decision
- [jev-browser (jkudish)](https://github.com/jkudish/jev-browser) `intent-routing` — browser-use experiment
- [JevTest](https://github.com/CorieW/JevTest) `other` — Bounded exploratory browser tests
- [unclutter](https://github.com/kitze/unclutter) `other` — Page clutter removal extension · [X](https://x.com/thekitze/status/2100595129874817340)
- [sift](https://github.com/tylergibbs1/sift) `composite-score` — Re-rank Google results with Jev
- [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) `intent-routing` — Zero-lock, session-preserving Chrome MCP server that couples a local Jev System One semantic micro-loop (`chrome_act_toward_goal`) with an 8
- [jev-browser-use](https://github.com/wy-coliney/jev-browser-use) `intent-routing` — Codex browser skill that uses Jev for navigation and target selection while Codex handles text entry and outcome verification.
- [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) `intent-routing` — Maps partial speech transcripts to browser intents and observed targets, with code deciding whether to act, wait, or ask.
- [ego-jev](https://github.com/jiangkoumo/ego-jev) `intent-routing` — Drive ego lite browser: one element table in, one op+target out
- [jev-browser (Ying-Kai-Liao)](https://github.com/Ying-Kai-Liao/jev-browser) `intent-routing` — LLM plans, Jev decides; library, CLI, MCP
- [jev-browse](https://github.com/0x7067/jev-browse) `intent-routing` — Browser automation with Jev as decision model
- [computer-use-jev](https://github.com/paulsmith/computer-use-jev) `intent-routing` — macOS computer use driven by Jev
- [JevBrowserExt](https://github.com/chy4pro/JevBrowserExt) `intent-routing` — Manifest V3 ultrafast browser automation extension
- [sf-autopilot](https://github.com/flxbl-io/sf-autopilot) `intent-routing` — LLM plans Salesforce steps; Jev chooses; Playwright executes
- [jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp) `other` — MCP wrapper around jev-ultrafast-style browser control
- [jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa) `other` — Frontend QA on Jev Ultrafast
- [jevbrow](https://github.com/timpratim/jevbrow) `other` — Codex/Claude Code browser skill on Jev Ultrafast
- [jev-computer-use](https://github.com/max1874/jev-computer-use) `intent-routing` — macOS port of jev-ultrafast indexed action space
- [typesafe-adblock](https://github.com/realZachi/typesafe-adblock) `confidence-gate` — Chrome extension: Jev noul is-this-DOM-node-an-ad
- [jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) `intent-routing` — Native Mac clicker loop via Jev
- [Winnow (ThinkyMiner)](https://github.com/ThinkyMiner/Winnow) `confidence-gate` — Chrome worth-it gate (distinct from GhalebDweikat/winnow)
- [tiptour-macos](https://github.com/milind-soni/tiptour-macos) `vision` — CoreML segment + on-device OCR + Jev click ~90ms · [X](https://x.com/milindsoni/status/2100631847155994852)
- [jev-mobile](https://github.com/Friedjof/jev-mobile) `confidence-gate` — USB Android observe/decide/mutate + MCP
- [otto](https://github.com/NobleSpartan6/otto) `vision` — Native macOS/Windows computer-use: Jev + local OCR
- [jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice) `other` — Windows voice control via Jev + UI Automation
- [jevdroid](https://github.com/antiyro/jevdroid) `other` — Android accessibility tree actions chosen by Jev
- [jev-turbo](https://github.com/sightmap/jev-turbo) `other` — Semantic browser use; Jev picks named actions
- [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) `other` — Jev action selection inside Codex Computer Use
- [jev-social](https://github.com/socai-io/jev-social) `other` — Jev picks browser steps for IG/TikTok/LinkedIn research

## Vision, images, and local eyes

- [Djev playground](https://djev.dev) `vision` — Maisa hosted preview: native images + webcam. Invite-only. Not TypeSafe.
- [Djev API docs](https://api.djev.dev/docs) `vision` — POST /v1/request with images[]; djev-0.1
- [djev-dev](https://github.com/Davipar/djev-dev) `vision` — Open DiffusionGemma Jev: images, image-as-options, camera · [X](https://x.com/davipar/status/2101363515663475176)
- [djev-spark](https://github.com/mmastrac/djev-spark) `vision` — DGX Spark Docker: webcam/hotdog/walk on DiffusionGemma-as-Jev · [X](https://x.com/mmastrac/status/2100984971372740760)
- [diffgemma](https://github.com/mmastrac/diffgemma) `vision` — Matt Mastracci DiffusionGemma playground (pre-djev) · [X](https://x.com/mmastrac/status/2100655582030262639)
- [mlx-vlm](https://github.com/jamescorbett/mlx-vlm) `vision` — Apple MLX DiffusionGemma-as-Jev (systemone)
- [PlayJev](https://github.com/OmniJev/PlayJev) `vision` — 0.8B Qwen: raw game frames → one move
- [jev_local](https://github.com/Argos1111/jev_local) `vision` — Local /v1/systemone with LFM2.5-VL image array
- [OpenJev-Vision](https://github.com/IamBusy/OpenJev-Vision) `vision` — DINOv2/CNN: real photos → noul/choice
- [PocketJev](https://github.com/NullPo-jp/PocketJev) `vision` — iPhone Qwen3-VL camera judgments
- [jevfire](https://github.com/kikoncuo/jevfire) `vision` — Jev-like inference on any model; accepts images
- [nothotdog](https://github.com/anishsrinivasan/nothotdog) `vision` — VLM caption then TypeSafe Jev (hotdog) · [X](https://x.com/anishsrinivasan/status/2101306033146847458)
- [jev-drive](https://github.com/eylexlive/jev-drive) `vision` — Gemini Vision vs sim state; Jev or Gemini drives
- [jevaluate](https://github.com/ElshinQ/jevaluate) `vision` — Jev picks clicks; DeepSeek reads screenshots for UI bugs
- [jev-clerk](https://github.com/stas4000/jev-clerk) `vision` — Mac accounting: OCR lines → Jev Choice
- [dating-booster](https://github.com/cyberpinkman/dating-booster) `vision` — Vision reads UI; Jev judges text · [X](https://x.com/cyberpink_x/status/2101590611010924741)
- [jev-paint](https://github.com/achimala/jev-paint) `vision` — Per-pixel Score distributions painted (generation, not seeing)
- [JevPixelArt](https://github.com/rivianpratama/JevPixelArt) `vision` — Jev Score per RGB(A) channel → pixel art
- [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) `vision` — 256 parallel pixel Choices; 16x16 fake diffusion

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
- [duckdb-jev](https://github.com/colliber/duckdb-jev) `other` — DuckDB extension that exposes Jev judgments as SQL values with return types derived from the declared criteria.
- [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) `other` — Streaming filter and scorer for Parquet and JSONL datasets.
- [jev-reviewer](https://github.com/choxos/jev-reviewer) `other` — Research-document extraction aid where Jev selects and verifies source lines for verbatim quotes; findings require human review and are not
- [jev-search](https://github.com/superagents-lab/jev-search) `other` — Uses Jev to select search sources and rank Search1API results, returning source links and snippets.
- [jev-trade](https://github.com/aowang-ai/jev-trade) `other` — Hyperliquid trading desk where Jev answers Choice questions for long/short, open/close/hold, and leverage; application code quotes or sends
- [jev-tree](https://github.com/reachjalil/jev-tree) `other` — Recursive choice over taxonomies larger than Jev's direct option limit.
- [jevql](https://github.com/kylemclaren/jevql) `other` — psql-shaped client and Go/TypeScript/Python SDKs for vanilla Postgres where Jev makes Noul, Choice, and Score judgements about individual ta
- [jevsql](https://github.com/EugeneBoondock/jevsql) `other` — SQL-like filtering, ranking, classification, and scoring with natural-language predicates.
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) `other` — LlamaIndex reranker and selector using Jev Score and Choice answers, with configurable confidence handling.
- [n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev) `other` — Community n8n node for asking multiple typed questions over workflow state.
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) `other` — Pre-alpha PostgreSQL C extension exposing Choice, Noul, Score, and batched judgments from SQL.
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) `other` — Classifies text-bearing PDF pages into IRS form and page-kind candidates with a confidence gate; document triage, not tax advice, and scanne
- [tiershift](https://github.com/iamvatsalpatel/tiershift) `other` — Policy-bounded model routing for TypeScript and Python.
- [jev-skip](https://github.com/valentynkit/jev-skip) `other` — Browser extension that reads the YouTube caption track and paints a per-segment sponsor probability on the seek bar before the intro ends, w
- [Jevthoven](https://github.com/cocktailpeanut/jevthoven) `other` — Symbolic-music studio where Jev chooses plans, instruments, and bar patterns, and code renders editable music and MIDI.
- [SlidePilot](https://github.com/harshil1712/slidepilot) `other` — Experimental Slidev controller that judges speech transcripts for slide completion, with deterministic checks and manual navigation.
- [Sponsor Skip](https://github.com/trungdq88/youtube-sponsor-detection) `other` — Finds sponsor reads in YouTube transcripts or transcribed audio while code owns timestamps and playback skipping.
- [Vibe Check for X](https://github.com/RafalWilinski/vibecheck) `other` — Chrome extension that scores draft posts and reply context before posting; optional media descriptions come from a separate vision model.
- [jev-voice](https://github.com/kevinbadi/jev-voice) `intent-routing` — Talk to your Mac: whisper.cpp + one Jev call per command
- [reranker](https://github.com/hev/reranker) `composite-score` — Calibrated reranker: one Jev call, up to 30 documents
- [jevplayground](https://github.com/terryds/jevplayground) `other` — Browser-only Jev playground via Vercel AI Gateway
- [jevmod](https://github.com/ohernandezdev/jevmod) `fan-out` — Moderation bots (Discord/Telegram/Reddit) with Jev probabilities
- [jev-typesafe-ai notes](https://github.com/codaaiteam/jev-typesafe-ai) `catalog` — Unofficial developer notes and examples for Jev
- [trade-jev](https://github.com/justinhe16/trade-jev) `intent-routing` — Backtest Jev as BUY/SELL/HOLD on NQ L10 order-book data
- [typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground) `other` — Playground for Jev / System One experiments
- [jev-academy](https://github.com/Btheriot83/jev-academy) `catalog` — Public zero-to-hero Jev / TypeSafe walkthrough
- [jev1](https://github.com/jflam/jev1) `intent-routing` — Smart-home assistant demo on Jev
- [should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all) `other` — Asks Jev whether AI should kill us all every ten minutes from headlines
- [jev-telegram-admin](https://github.com/Zumka1991/jev-telegram-admin) `intent-routing` — Telegram group moderator powered by Jev
- [jev-x-posts](https://github.com/samoweb3/jev-x-posts) `composite-score` — 48-hour X post report for Jev with sentiment labels
- [jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control) `intent-routing` — Mac menu-bar: speech to Jev typed decisions to macOS actions
- [stanley](https://github.com/armansra-hub/stanley) `other` — NetSuite AE territory intelligence: Jev interprets company evidence
- [potpie-doc-parser](https://github.com/0xSarnavo/potpie-doc-parser) `other` — Extractive docs search powered by Jev, no generated text
- [omarchy-issue-classifier](https://github.com/robzolkos/omarchy-issue-classifier) `fan-out` — Ten typed questions per Omarchy issue in one Jev request
- [polymarket-btc-5m-agent](https://github.com/BrunooMoniz/polymarket-btc-5m-agent) `confidence-gate` — Polymarket BTC 5m agent: code model, Jev as gate
- [ask-jev-ai](https://github.com/waynesutton/ask-jev-ai) `other` — Public wall: 3-15 word questions, yes/no/depends in ~100ms
- [typesafe-assist](https://github.com/JanOstrowka/typesafe-assist) `intent-routing` — Home Assistant Assist conversation agent using Jev
- [typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard) `confidence-gate` — DDL safety gate via Jev SAFE/DANGER
- [vgi-typesafe](https://github.com/Query-farm/vgi-typesafe) `client` — DuckDB/SQL table functions wrapping System One questions
- [new-api-plugin-typesafe](https://github.com/FFatTiger/new-api-plugin-typesafe) `client` — new-api plugin for native /v1/systemone
- [jevinci](https://github.com/achimala/jevinci) `other` — Use Jev to make art
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) `other` — grep-by-meaning scored by TypeSafe Jev
- [jevocks](https://github.com/unicodeveloper/jevocks) `other` — Everyday stocks status with Jev
- [jev-chat (w3cj)](https://github.com/w3cj/jev-chat) `other` — Tool-calling chatbot with Jev and no LLM
- [newsjack](https://github.com/elvisun/newsjack) `composite-score` — PR agent: Jev ranks news for brands
- [triage-bot](https://github.com/TheEleventhAvatar/triage-bot) `intent-routing` — Jev classifies tickets; Cerebras drafts reply
- [worth-replying](https://github.com/AIsa-team/worth-replying) `confidence-gate` — Reply-worthiness gate
- [Jevons](https://github.com/jevonsdev/Jevons) `other` — Jev-driven buyback/burn on Robinhood Chain
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) `other` — TypeSafe Jev recipes on OpenRouter
- [embodied-jev](https://github.com/FBddcz/embodied-jev) `other` — MuJoCo Franka; Jev or MiniCPM/OpenAI vision
- [classifier-dev](https://github.com/mrmps/classifier-dev) `intent-routing` — Packed zero-shot text classification via jev-latest
- [jevlergy](https://github.com/daisuke7/jevlergy) `other` — Allergen detector via Jev
- [senseek](https://github.com/liou666/senseek) `other` — Cheap semantic find via Jev
- [mysql-ailike](https://github.com/maayanlevy/mysql-ailike) `other` — MySQL row filter with Jev meaning
- [jev-latam-lead-triage](https://github.com/integralmarketingmx/jev-latam-lead-triage) `intent-routing` — Spanish WhatsApp/CRM lead triage

## Games and simulations

- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) `intent-routing` — Mario from structured emulator state
- [typesafe-snake](https://github.com/sorrycc/typesafe-snake) `intent-routing` — One typed decision per tick
- [heist-one](https://github.com/AbdelStark/heist-one) `other` — Jev judges guards; code owns world
- [jev-drone](https://github.com/RomanSlack/jev-drone) `other` — MuJoCo quadrotor tactical Jev
- [tsai-sc](https://github.com/phyous/tsai-sc) `intent-routing` — StarCraft shareware via Jev
- [jev-little-airways](https://github.com/lbotinelly/jev-little-airways) `fan-out` — ATC divert/hold/clearance live
- [jev-chat](https://github.com/adhyaay-karnwal/jev-chat) `other` — Wrong-use study: chat from Choices
- [jev-canvas](https://github.com/gaborishka/jev-canvas) `intent-routing` — Voice and finger-pointing control of a tldraw canvas: Jev picks the action, target shape and place from each partial transcript plus the fin
- [jev-experiments](https://github.com/dabit3/jev-experiments) `intent-routing` — Collection of inspectable Jev demos, including scripted support conversations with typed intent, escalation, and suggested-response decision
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) `intent-routing` — Pokemon Red on PyBoy where deterministic code owns the route and arithmetic and Jev picks only at branches, with every battle turn's faint p
- [JevPilot](https://github.com/standardagents/jevpilot) `intent-routing` — Three.js driving simulation where Jev chooses among candidate paths and speeds while local code handles vehicle dynamics and geometry.
- [JevScape](https://github.com/Skyvern-AI/jevscape) `intent-routing` — RuneBench-based RuneScape harness that maps Jev choices to a bounded game-action catalog and records tick-level results.
- [jev-craft](https://github.com/akash-kamat/jev-craft) `intent-routing` — Minecraft survival bot that thinks with Jev
- [jevball](https://github.com/atarikcaliskan/jevball) `fan-out` — 3D football: every player is its own Jev decision
- [typesafe-nes](https://github.com/seanthomasevans/typesafe-nes) `intent-routing` — Jev plays Mario, Contra, Mega Man via stable-retro
- [jev-poker](https://github.com/meetr1912/jev-poker) `intent-routing` — Heads-up NLHE with decision probabilities on the side panel
- [jev-got](https://github.com/phureewat29/jev-got) `other` — Jev PoC through Game of Thrones
- [magi-system-on-jev](https://github.com/hide-G/magi-system-on-jev) `fan-out` — MAGI three-sage deliberation rebuilt with Jev
- [jev-gamebenchmark](https://github.com/aieo-product/jev-gamebenchmark) `other` — Falling-block puzzle sandbox: Jev vs LLMs
- [haikyuBattleJev](https://github.com/aoi-yoneda/haikyuBattleJev) `intent-routing` — Baseball pitch-call simulation judged by Jev
- [jevspace](https://github.com/imserhatdemir/jevspace) `intent-routing` — DarkOrbit-style Three.js space game piloted by Jev
- [chakravyuha-jev](https://github.com/kspviswa/chakravyuha-jev) `intent-routing` — Polar ring-maze where every move is a Jev decision
- [JevPiano](https://github.com/charleeagni/JevPiano) `other` — TypeSafe Jev + jev-ultrafast real-time piano controller
- [live-jev](https://github.com/vinilana/live-jev) `other` — Browser 2D car sim driven by TypeSafe Jev
- [jev-game-agent](https://github.com/IAnMove/jev-game-agent) `intent-routing` — Mario RAM+lookahead Jev agent
- [rubikjev](https://github.com/0xtrou/rubikjev) `other` — Jev 3x3 cube solver
- [Parsewell](https://github.com/Shurikal/Parsewell) `other` — Batched Jev call per text-adventure move
- [mario-jev](https://github.com/shantanugoel/mario-jev) `intent-routing` — Mario via Jev
- [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) `intent-routing` — Pokemon Red typed questions
- [river-run-typesafe](https://github.com/ashaazami/river-run-typesafe) `other` — River Raid shooter; Jev picks lane and fire
- [OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) `other` — 1v1 quickscope arena; Jev vs human

## Open replicas and evals

- [openjev (TheoLeeCJ)](https://github.com/TheoLeeCJ/openjev) `other` — Jev-like on a 3090 at home · [X](https://x.com/hhkkmon/status/2100443314957038010)
- [openjev (razorback16)](https://github.com/razorback16/openjev) `client` — Jev-compatible server on DiffusionGemma
- [system-one-gemma](https://github.com/akash-kamat/system-one-gemma) `other` — Open scoring head on Gemma 3 270M
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) `other` — Blind prompt-injection + vuln code · [X](https://x.com/_GauravGosain/status/2100111398277959715)
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) `other` — Calibration, selective risk, latency
- [jev-korean-benchmark](https://github.com/mahlernim/jev-korean-benchmark) `other` — Korean understanding / medical text
- [jevmlx](https://github.com/bnsd55/jevmlx) `other` — Parallel decisions on Apple MLX · [X](https://x.com/beni_il_/status/2100617387116568956)
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) `client` — Jev-compatible endpoint, open models
- [Jev Visual](https://github.com/hr98w/jev-visual) `other` — Educational MLX/Qwen vision-language experiment sharing image context across candidate-scoring questions; its probabilities are not calibrat
- [Jevlike](https://github.com/vinnylarouge/jevlike) `other` — Trainable encoder and option-attention head for variable candidate sets, with separate visual game experiments.
- [LitJev](https://github.com/zhengxuyu/litjev) `other` — Reproduction of Jev that turns any Qwen model into a fast decision model, serving the same `/v1/systemone` schema (Choice, Score, Noul) with
- [kev](https://github.com/jaredpalmer/kev) `other` — Qwen2.5-0.5B adapter and decision head with training code, released weights, and parallel typed-question inference.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) `other` — Small parallel-decision model with dynamic candidates, a training pipeline, and recorded game comparisons that include shared code planning.
- [openjev](https://github.com/zhihz/openjev) `other` — Local bilingual probability decisions from context, questions, and candidate answers.
- [openvons](https://github.com/genai-craft/openvons) `other` — Open decision layer for finite options across text, images, and Japanese voice commands.
- [parallelConstraintDecoding](https://github.com/stephanj/parallelConstraintDecoding) `other` — Java and llama.cpp experiments in parallel constrained decoding.
- [reflex](https://github.com/kshetrajna12/reflex) `other` — Open-model decision engine with shared-state inference, isolated question branches, and a WebGPU demo; browser and Python configurations dif
- [SemIf](https://github.com/TheoLeeCJ/SemIf) `other` — Formerly OpenJev: an independent study of typed option readout from frozen open models, with shared-prefix experiments and a WebGPU demo.
- [Simple Jev](https://github.com/featherless-ai/simple-jev) `other` — Transforms compatible open-model logits into typed decisions without a separately trained classifier head; model compatibility is constraine
- [Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) `other` — ModernBERT decision engine with calibrated uncertainty and a WebGPU playground.
- [Janus](https://github.com/FirasSX914/Janus) `other` — Measures when to use Jev versus other models and routes accordingly.
- [jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study) `other` — Independent synthetic-task study of Jev 1.13.0 framing sensitivity and failures, with raw responses and offline report checks.
- [jev-eval](https://github.com/4esv/jev-eval) `other` — Independent Jev versus GPT-5.6 Terra comparison on three labeled classification tasks, reporting accuracy, calibration, latency, and cost.
- [jev-eval-agent](https://github.com/vinilana/jev-eval-agent) `other` — Compares LLM tool selection with Jev routing in a personal-assistant harness containing 100 mocked tools.
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) `other` — Measures whether ORDER BY over a Jev probability is defensible (inversion rate, Score ordinality against a human grade, calibration, wording
- [jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) `other` — Chinese/English retrieval evaluation comparing Jev reranking with lexical, embedding, and fusion baselines, including judge-circularity anal
- [jevcal](https://github.com/abhixhek/jevcal) `other` — Fits and drift-checks confidence thresholds against labeled data.
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) `other` — LLM gateway that mimics the System One output shape for comparison work.
- [jev-visual (kevin9327)](https://github.com/kevin9327/jev-visual) `other` — User repo: educational Jev-like visual inference on Apple Silicon
- [localjev](https://github.com/githubnext/localjev) `other` — GitHub Next local Jev-like decision model
- [jev-exploration](https://github.com/SamuelSacco/jev-exploration) `other` — Claim audit, live demos, and runnable Jev code
- [jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) `other` — Calibration and selective-risk benchmarks in DSPy workflows
- [jevx](https://github.com/umgbhalla/jevx) `other` — API notes, benchmarks, and agent-loop experiments
- [jev-synergy-screening](https://github.com/PistachioAIHQ/jev-synergy-screening) `other` — ASReview SYNERGY abstract screening: Choice/Noul vs gold labels
- [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) `other` — Jev vs Claude Haiku 4.5 on 2000 phishing emails
- [jevassert](https://github.com/dtduc-git/jevassert) `other` — Record/replay regression tests for Jev question packs
- [jev-ja-eval](https://github.com/uesgugikouhei-oss/jev-ja-eval) `other` — Japanese customer-inquiry eval: Jev vs LLM vs rules
- [jev-tick-lab](https://github.com/shunta-furukawa/jev-tick-lab) `other` — One-second trading judgments on bitbank, logged for calibration
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) `other` — Jev vs LLM on Who&When Pro agent-failure attribution
- [instruct-jev](https://github.com/ctaxnagomi/instruct-jev) `other` — INSTRUCT_JEV choice/noul/score instruction corpus
- [jev-judge-bench](https://github.com/cmartinez9/jev-judge-bench) `other` — Binary LLM-judge bench: Jev vs frontier judge
- [jev-anotacao-sentencas](https://github.com/lab-dados/jev-anotacao-sentencas) `other` — Jev vs Gemini vs GPT on TJSP sentence annotation
- [dual-process-ai](https://github.com/taro1985/dual-process-ai) `other` — System 1 Jev + System 2 Gemini design pattern
- [jev-jp-address](https://github.com/smasato/jev-jp-address) `other` — KEN_ALL Japanese address fuzzy-match eval via Jev
- [jeff](https://github.com/logan-markewich/jeff) `client` — Self-hosted GLiFormer drop-in for TypeSafe Jev API
- [jev-research-eval](https://github.com/jgridifier/jev-research-eval) `other` — Reproducible Jev Ultrafast research-browser eval
- [open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) `other` — Packed one-pass typed decisions from open LLMs
- [jev-vs-llm](https://github.com/BUNYOD0987/jev-vs-llm) `other` — Jev vs GPT-5.6 Luna vs Sonnet 5 ticket bench
- [systemone-lite](https://github.com/fritzprix/systemone-lite) `other` — Toy local System One-style decision API
- [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) `other` — Evidence map of where Jev holds or breaks
- [laya](https://github.com/NandhaKishorM/laya) `other` — Non-AR RLCD decision model
- [jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) `other` — Local Jev-like parallel decisions on a laptop
- [nimble](https://github.com/bespokelabsai/nimble) `other` — Open model matching Jev-ish performance
- [laya-mlx](https://github.com/mizorewww/laya-mlx) `other` — Local System One on MLX · [X](https://x.com/mizorewww/status/2101473552956555427)
- [laya-coreml](https://github.com/mizorewww/laya-coreml) `other` — Apple Silicon CoreML System One
- [poorjev](https://github.com/rupeshpoojary9/poorjev) `other` — Zero-shot NLI Choice/Score/Noul
- [jev_benchmark](https://github.com/ywchiu/jev_benchmark) `catalog` — Open measured Jev vs others
- [jev-align](https://github.com/sutro-sh/jev-align) `other` — GEPA: label uncertain examples, improve Jev questions

## Other directories

- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) `catalog` — Source-backed curated list
- [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) `catalog` — Large directory + awesomejev.com
- [awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) `catalog` — Evidence-backed use cases
- [awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) `catalog` — Official + community index
- [awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) `catalog` — Patterns, prompts, starter code
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) `catalog` — Field guide by decision domain
- [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) `catalog` — Directory + X posts
- [OmniJev/awesome-jev](https://github.com/OmniJev/awesome-jev) `catalog` — Papers, open reproductions, independent evaluations, and technical lineage.
- [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) `catalog` — CC0, awesome-lint clean, sorted by what you would install, with a short know-before-you-build section on the limits.
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) `catalog` — Source-backed ecosystem radar with automatic GitHub sync
- [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) `catalog` — Curated Jev / System One applications and libraries
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) `catalog` — Source-backed directory plus reusable Jev GitHub review workflow
- [jev-atlas](https://github.com/gorock007/jev-atlas) `catalog` — Independent evidence-first field guide to Jev
- [jevsome-projects](https://github.com/ozers/jevsome-projects) `catalog` — Projects that provably call Jev, with line-of-code evidence
- [jev-radar](https://github.com/everyinfra/jev-radar) `catalog` — Ecosystem tracker of documented Jev cases, rescanned on a timer
- [jev-hub](https://github.com/mizzlelover/jev-hub) `catalog` — Chinese index of Jev demos and articles

## X threads

- [@typesafeai](https://x.com/typesafeai) `catalog` — Official product/research posts
- [Vercel AI Gateway Jev](https://x.com/typesafeai/status/2100376436272173088) `client` — Hosted typesafe-ai/jev, no waitlist
- [Browser Use ultrafast](https://x.com/gregpr07/status/2100411066966749359) `intent-routing` — Jev picks browser op + element
- [jev-trader on X](https://x.com/jarrodwatts/status/2100356151468585346) `intent-routing` — On-chain Jev trade loop
- [Logicrw field roundup](https://x.com/0xLogicrw/status/2100478725393686556) `catalog` — Roundup of neo4jev, review, MCP, winnow
- [Jev launch (Diogo Almeida)](https://x.com/CompleteSkeptic/status/2099925682726002904) `catalog` — Canonical Jev launch: RLCD, decision model not chat
- [Jev on OpenRouter](https://x.com/typesafeai/status/2100747035746193598) `client` — Official OpenRouter beta listing
- [Jev on Cloudflare AI Gateway](https://x.com/typesafeai/status/2100700021700378803) `client` — Official Cloudflare AI Gateway partnership
- [Jev on Venice API](https://x.com/AskVenice/status/2101095644467511578) `client` — Venice API beta: typed answers for code branching
- [OpenRouter Jev beta](https://x.com/OpenRouter/status/2100744709589316009) `client` — Partner launch: state + typed question, no JSON parse
- [jevis Flutter package](https://x.com/jake_gwon/status/2101194639948787818) `client` — Flutter integration tests in natural language via Jev
- [localjev + openjev roundup](https://x.com/ersinkoc/status/2101229864305009124) `catalog` — Points at razorback16/openjev and githubnext/localjev
- [Open System One models](https://x.com/hhkkmon/status/2101219943744499783) `catalog` — Community roundup of local Jev-like models
- [ego-jev on X](https://x.com/jiangkoumo_/status/2101224137360654698) `intent-routing` — ego-jev open-source browser driver aligned with jev-ultrafast
- [y0usaf typesafe-mcp on X](https://x.com/realy0usaf/status/2100106949874335851) `client` — Community MCP evaluate(state, questions)
- [tumf jev-cli on X](https://x.com/DevTumf/status/2101071184855261563) `client` — Unofficial CLI+stdio MCP
- [AbdelStark awesome-typesafe on X](https://x.com/AbdelStark/status/2100524358254911889) `catalog` — Launch of awesome-typesafe community index
- [Foreman OSS on X](https://x.com/JoshARosen/status/2100573432089866717) `confidence-gate` — thruwire/foreman: Jev supervises coding agents
- [openjev community writeup](https://x.com/hhkkmon/status/2100443314957038010) `other` — Community writeup of TheoLeeCJ/openjev
- [jev-craft on X](https://x.com/_akashkamat/status/2101208666074751136) `intent-routing` — Minecraft survival bot thinking with Jev
- [fast-jev-compaction on X](https://x.com/jreuben1/status/2101180061172826143) `confidence-gate` — Claude Code plugin: Jev keep/drop tool results
- [quackd on X](https://x.com/rokbenko/status/2101212301076414660) `intent-routing` — LeRobot SO-101 via quackd --jev on
- [newsjack on X](https://x.com/RoundtableSpace/status/2101253717689340320) `composite-score` — PR agent ranks news with Jev
- [TechCrunch Jev](https://x.com/TechCrunch/status/2101022221774856412) `catalog` — Press: cheaper/faster software intelligence
- [Vercel Developers Jev](https://x.com/vercel_dev/status/2100378959653507175) `client` — evaluate({ model: typesafe-ai/jev })
- [OpenRouter decision model primer](https://x.com/OpenRouter/status/2101061688338575739) `intent-routing` — Partner primer: yes/no and multiple-choice with confidence
- [Djev how-to-images thread](https://x.com/LukeberryPi/status/2101307264829149210) `vision` — Canonical X thread: how to make Jev process images
- [TypeSafe wait-a-while](https://x.com/dotpem/status/2101335033609138382) `vision` — Official TypeSafe: Jev images not yet; wait a while
- [djev-dev launch](https://x.com/davipar/status/2101363515663475176) `vision` — davipar Djev launch: native image input and image options
- [mmastrac phone vision](https://x.com/mmastrac/status/2101011110132601054) `vision` — DiffusionGemma-as-Jev live phone vision / stairs

## What jev-master adds

Link directories stop at the URL. This repo ships a live `POST /v1/systemone` client, mixed Choice+Score+Noul, compose apps (ticket/gate/pitch plus JevBot/JevHarness/JevCode), JevBrowser, and tests on the shipped builders — then points at the rest of the field.


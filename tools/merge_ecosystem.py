"""Append missing Jev-field citations into docs/ecosystem.json. No clones."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "ecosystem.json"

NEW: list[dict[str, str]] = [
    # Djev / Maisa (not TypeSafe)
    {"name": "Djev playground", "url": "https://djev.dev", "kind": "vision", "pattern": "vision", "note": "Maisa hosted preview: native images + webcam. Invite-only. Not TypeSafe."},
    {"name": "Djev API docs", "url": "https://api.djev.dev/docs", "kind": "vision", "pattern": "vision", "note": "POST /v1/request with images[]; djev-0.1"},
    {"name": "djev-dev", "url": "https://github.com/Davipar/djev-dev", "kind": "vision", "pattern": "vision", "note": "Open DiffusionGemma Jev: images, image-as-options, camera", "x": "https://x.com/davipar/status/2101363515663475176"},
    {"name": "djev-spark", "url": "https://github.com/mmastrac/djev-spark", "kind": "vision", "pattern": "vision", "note": "DGX Spark Docker: webcam/hotdog/walk on DiffusionGemma-as-Jev", "x": "https://x.com/mmastrac/status/2100984971372740760"},
    {"name": "diffgemma", "url": "https://github.com/mmastrac/diffgemma", "kind": "vision", "pattern": "vision", "note": "Matt Mastracci DiffusionGemma playground (pre-djev)", "x": "https://x.com/mmastrac/status/2100655582030262639"},
    {"name": "openjev (razorback16)", "url": "https://github.com/razorback16/openjev", "kind": "vision", "pattern": "vision", "note": "DiffusionGemma Jev-compatible server; up to 8 images"},
    {"name": "mlx-vlm", "url": "https://github.com/jamescorbett/mlx-vlm", "kind": "vision", "pattern": "vision", "note": "Apple MLX DiffusionGemma-as-Jev (systemone)"},
    # Local VL / pixel models
    {"name": "PlayJev", "url": "https://github.com/OmniJev/PlayJev", "kind": "vision", "pattern": "vision", "note": "0.8B Qwen: raw game frames → one move"},
    {"name": "jev_local", "url": "https://github.com/Argos1111/jev_local", "kind": "vision", "pattern": "vision", "note": "Local /v1/systemone with LFM2.5-VL image array"},
    {"name": "OpenJev-Vision", "url": "https://github.com/IamBusy/OpenJev-Vision", "kind": "vision", "pattern": "vision", "note": "DINOv2/CNN: real photos → noul/choice"},
    {"name": "PocketJev", "url": "https://github.com/NullPo-jp/PocketJev", "kind": "vision", "pattern": "vision", "note": "iPhone Qwen3-VL camera judgments"},
    {"name": "openvons", "url": "https://github.com/genai-craft/openvons", "kind": "vision", "pattern": "vision", "note": "Frozen vision encoder + small decision head"},
    {"name": "jevfire", "url": "https://github.com/kikoncuo/jevfire", "kind": "vision", "pattern": "vision", "note": "Jev-like inference on any model; accepts images"},
    {"name": "reflex (kshetrajna12)", "url": "https://github.com/kshetrajna12/reflex", "kind": "research", "pattern": "vision", "note": "Open vision-Jev alternative vs DiffusionGemma"},
    # TypeSafe + rented eye (OCR/caption)
    {"name": "nothotdog", "url": "https://github.com/anishsrinivasan/nothotdog", "kind": "vision", "pattern": "vision", "note": "VLM caption then TypeSafe Jev (hotdog)", "x": "https://x.com/anishsrinivasan/status/2101306033146847458"},
    {"name": "jev-drive", "url": "https://github.com/eylexlive/jev-drive", "kind": "vision", "pattern": "vision", "note": "Gemini Vision vs sim state; Jev or Gemini drives"},
    {"name": "jevaluate", "url": "https://github.com/ElshinQ/jevaluate", "kind": "vision", "pattern": "vision", "note": "Jev picks clicks; DeepSeek reads screenshots for UI bugs"},
    {"name": "jev-clerk", "url": "https://github.com/stas4000/jev-clerk", "kind": "vision", "pattern": "vision", "note": "Mac accounting: OCR lines → Jev Choice"},
    {"name": "tiptour-macos", "url": "https://github.com/milind-soni/tiptour-macos", "kind": "browser", "pattern": "vision", "note": "CoreML segment + on-device OCR + Jev click ~90ms", "x": "https://x.com/milindsoni/status/2100631847155994852"},
    {"name": "dating-booster", "url": "https://github.com/cyberpinkman/dating-booster", "kind": "vision", "pattern": "vision", "note": "Vision reads UI; Jev judges text", "x": "https://x.com/cyberpink_x/status/2101590611010924741"},
    {"name": "jev-paint", "url": "https://github.com/achimala/jev-paint", "kind": "vision", "pattern": "vision", "note": "Per-pixel Score distributions painted (generation, not seeing)"},
    {"name": "JevPixelArt", "url": "https://github.com/rivianpratama/JevPixelArt", "kind": "vision", "pattern": "vision", "note": "Jev Score per RGB(A) channel → pixel art"},
    {"name": "typesafe-image-diffusion", "url": "https://github.com/Wizhill05/typesafe-image-diffusion", "kind": "vision", "pattern": "vision", "note": "256 parallel pixel Choices; 16x16 fake diffusion"},
    {"name": "embodied-jev", "url": "https://github.com/FBddcz/embodied-jev", "kind": "app", "pattern": "other", "note": "MuJoCo Franka; Jev or MiniCPM/OpenAI vision"},
    {"name": "classifier-dev", "url": "https://github.com/mrmps/classifier-dev", "kind": "app", "pattern": "intent-routing", "note": "Packed zero-shot text classification via jev-latest"},
    {"name": "river-run-typesafe", "url": "https://github.com/ashaazami/river-run-typesafe", "kind": "game", "pattern": "other", "note": "River Raid shooter; Jev picks lane and fire"},
    {"name": "OneVOneJev", "url": "https://github.com/emrickgarrett/OneVOneJev", "kind": "game", "pattern": "other", "note": "1v1 quickscope arena; Jev vs human"},
    # Computer use / mobile
    {"name": "mobile-jev", "url": "https://github.com/droidrun/mobile-jev", "kind": "browser", "pattern": "confidence-gate", "note": "Android Mobilerun; Jev decides each step"},
    {"name": "jev-mobile", "url": "https://github.com/Friedjof/jev-mobile", "kind": "browser", "pattern": "confidence-gate", "note": "USB Android observe/decide/mutate + MCP"},
    {"name": "otto", "url": "https://github.com/NobleSpartan6/otto", "kind": "browser", "pattern": "vision", "note": "Native macOS/Windows computer-use: Jev + local OCR"},
    {"name": "jev-windows-voice", "url": "https://github.com/mstf-svndk/jev-windows-voice", "kind": "browser", "pattern": "other", "note": "Windows voice control via Jev + UI Automation"},
    {"name": "jevdroid", "url": "https://github.com/antiyro/jevdroid", "kind": "browser", "pattern": "other", "note": "Android accessibility tree actions chosen by Jev"},
    {"name": "jev-turbo", "url": "https://github.com/sightmap/jev-turbo", "kind": "browser", "pattern": "other", "note": "Semantic browser use; Jev picks named actions"},
    {"name": "jev-desktop", "url": "https://github.com/yikangy873-gif/jev-desktop", "kind": "browser", "pattern": "other", "note": "Jev action selection inside Codex Computer Use"},
    # Local clones / open System One
    {"name": "SemIf (OpenJev)", "url": "https://github.com/TheoLeeCJ/SemIf", "kind": "research", "pattern": "other", "note": "Former OpenJev; logit-scoring replica"},
    {"name": "kev", "url": "https://github.com/jaredpalmer/kev", "kind": "research", "pattern": "other", "note": "Qwen LoRA serving /v1/systemone"},
    {"name": "openjev-sglang", "url": "https://github.com/ekzhang/openjev-sglang", "kind": "research", "pattern": "other", "note": "Prefill-only Jev-compatible API on SGLang"},
    {"name": "jeff", "url": "https://github.com/logan-markewich/jeff", "kind": "research", "pattern": "other", "note": "Self-hosted Jev via GliFormer"},
    {"name": "nimble", "url": "https://github.com/bespokelabsai/nimble", "kind": "research", "pattern": "other", "note": "Open model matching Jev-ish performance"},
    {"name": "laya-mlx", "url": "https://github.com/mizorewww/laya-mlx", "kind": "research", "pattern": "other", "note": "Local System One on MLX", "x": "https://x.com/mizorewww/status/2101473552956555427"},
    {"name": "laya-coreml", "url": "https://github.com/mizorewww/laya-coreml", "kind": "research", "pattern": "other", "note": "Apple Silicon CoreML System One"},
    {"name": "NanoJev", "url": "https://github.com/TianyuCodings/NanoJev", "kind": "research", "pattern": "other", "note": "0.6B parallel-decision replica; ViZDoom"},
    {"name": "poorjev", "url": "https://github.com/rupeshpoojary9/poorjev", "kind": "research", "pattern": "other", "note": "Zero-shot NLI Choice/Score/Noul"},
    {"name": "jev-on-a-laptop", "url": "https://github.com/rorshopping/jev-on-a-laptop", "kind": "research", "pattern": "other", "note": "Jev-style decisions on 1.5B–8B laptop models"},
    # Apps from X harvest 2026-09-20
    {"name": "jev_benchmark", "url": "https://github.com/ywchiu/jev_benchmark", "kind": "research", "pattern": "catalog", "note": "Open measured Jev vs others"},
    {"name": "jevlergy", "url": "https://github.com/daisuke7/jevlergy", "kind": "app", "pattern": "other", "note": "Allergen detector via Jev"},
    {"name": "jevcache", "url": "https://github.com/kushals256/jevcache", "kind": "agent", "pattern": "other", "note": "Skip duplicate LLM calls when Jev says same intent"},
    {"name": "senseek", "url": "https://github.com/liou666/senseek", "kind": "app", "pattern": "other", "note": "Cheap semantic find via Jev"},
    {"name": "mysql-ailike", "url": "https://github.com/maayanlevy/mysql-ailike", "kind": "app", "pattern": "other", "note": "MySQL row filter with Jev meaning"},
    {"name": "jev-s", "url": "https://github.com/wuyoscar/jev-s", "kind": "agent", "pattern": "other", "note": "Codex/Claude/OpenCode Jev skills bundle"},
    {"name": "agent-xray", "url": "https://github.com/morlex01/agent-xray", "kind": "agent", "pattern": "other", "note": "Jev analyzes agent traces into a Fix Pack"},
    {"name": "jev-social", "url": "https://github.com/socai-io/jev-social", "kind": "browser", "pattern": "other", "note": "Jev picks browser steps for IG/TikTok/LinkedIn research"},
    {"name": "jev-align", "url": "https://github.com/sutro-sh/jev-align", "kind": "research", "pattern": "other", "note": "GEPA: label uncertain examples, improve Jev questions"},
    {"name": "jev-semgrep", "url": "https://github.com/uehaj/jev-semgrep", "kind": "agent", "pattern": "other", "note": "Semantic grep via Jev instead of regex"},
    {"name": "tax-doc-classifier", "url": "https://github.com/kyotofin/tax-doc-classifier", "kind": "app", "pattern": "intent-routing", "note": "PDF pages → 261 IRS forms"},
    {"name": "n8n-nodes-jev-systemone", "url": "https://github.com/withabdul/n8n-nodes-jev-systemone", "kind": "sdk", "pattern": "client", "note": "n8n classify/score then IF/Switch"},
    {"name": "jev-pii-guardrail", "url": "https://github.com/jms-dcksn/jev-pii-guardrail", "kind": "agent", "pattern": "confidence-gate", "note": "PII detect around LLM calls"},
    {"name": "jev-latam-lead-triage", "url": "https://github.com/integralmarketingmx/jev-latam-lead-triage", "kind": "app", "pattern": "intent-routing", "note": "Spanish WhatsApp/CRM lead triage"},
    {"name": "typesafe-sdk-ruby (afurm)", "url": "https://github.com/afurm/typesafe-sdk-ruby", "kind": "sdk", "pattern": "client", "note": "Community Ruby TypeSafe client"},
    {"name": "Djev how-to-images thread", "url": "https://x.com/LukeberryPi/status/2101307264829149210", "kind": "x", "pattern": "vision", "note": "Canonical X thread: how to make Jev process images"},
    {"name": "TypeSafe wait-a-while", "url": "https://x.com/dotpem/status/2101335033609138382", "kind": "x", "pattern": "vision", "note": "Official TypeSafe: Jev images not yet; wait a while"},
    {"name": "djev-dev launch", "url": "https://x.com/davipar/status/2101363515663475176", "kind": "x", "pattern": "vision", "note": "davipar Djev launch: native image input and image options"},
    {"name": "mmastrac phone vision", "url": "https://x.com/mmastrac/status/2101011110132601054", "kind": "x", "pattern": "vision", "note": "DiffusionGemma-as-Jev live phone vision / stairs"},
]


def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    seen = {str(e.get("url") or "") for e in data["entries"]}
    added = 0
    for item in NEW:
        url = item["url"]
        if url in seen:
            continue
        data["entries"].append(item)
        seen.add(url)
        added += 1
    data["date"] = "2026-09-20"
    data["surveyed"] = (
        "GitHub awesome-jev lists, GitHub search, official TypeSafe + Djev docs, "
        "and X posts (image/vision harvest + 2026-09-20 field sweep)"
    )
    sources = list(data.get("sources") or [])
    extra_src = [
        "https://djev.dev",
        "https://github.com/Davipar/djev-dev",
        "https://github.com/mmastrac/djev-spark",
        "https://x.com/LukeberryPi/status/2101307264829149210",
        "https://jevbest.com/",
    ]
    for src in extra_src:
        if src not in sources:
            sources.append(src)
    data["sources"] = sources
    CATALOG.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"added {added} · total {len(data['entries'])}")


if __name__ == "__main__":
    main()

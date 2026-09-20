<p align="center">
  <img src="docs/assets/live-run.png" alt="실제 Jev 호출: POST /v1/systemone, Choice + Score + Noul" width="100%">
</p>

<p align="center">
  <strong><a href="README.md">English</a></strong>
  &nbsp;·&nbsp;
  <strong><a href="README.ko.md">한국어</a></strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/model-jev--latest-14b8a6" alt="jev-latest">
  <img src="https://img.shields.io/badge/POST-/v1/systemone-0f766e" alt="System One">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-5eead4" alt="MIT">
  <img src="https://img.shields.io/badge/catalog-382_by_kind-134e4a" alt="분류 382">
</p>

# jev-master

**상태를 넣고, 타입이 있는 답을 받고, 분기는 코드가 합니다.**

[TypeSafe Jev](https://docs.typesafe.ai/concepts/system-one)는 챗봇이 아닙니다. **판단할 내용(state)** 과 **질문(questions)** 을 보내면 Choice / Score / Noul 확률이 돌아옵니다. 이 저장소는:

1. **실행** — 조합 앱 7개와 실제 `POST /v1/systemone` 클라이언트.
2. **분류 목록** — 공개 프로젝트 382개를 종류별로 인용 ([`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md)). 링크만 있고 클론하지 않습니다.

위 화면은 `examples/stripe-ticket.txt`에 대한 실제 `jev-1.13.0` 호출 → `act` / `billing_priority_queue`. JSON: [`docs/assets/live-run.json`](docs/assets/live-run.json).

TypeSafe와 무관합니다. 이미지가 되는 [Djev](https://djev.dev)는 Maisa 제품입니다.

---

## 분류별로 보기

### A. 이 저장소 앱 (직접 실행)

| 분류 | 명령 | 이럴 때 |
| --- | --- | --- |
| **라우팅** | `python -m jev_master ticket --state examples/stripe-ticket.txt` | 어느 부서·대기열? |
| **확신 게이트** | `python -m jev_master gate --state examples/voice-command.txt` | 실행 / 사람 확인 / 에스컬레이션? |
| **점수** | `python -m jev_master pitch --state examples/pitch.txt` | 라벨 하나가 아니라 0~1 가중합 |
| **고정 봇** | `python -m jev_master bot --state examples/stripe-ticket.txt` | `reply` / `escalate` / `block` (채팅 LLM 아님) |
| **도구 하네스** | `python -m jev_master harness --state examples/rm-step.json` | 에이전트 도구: `execute` / `confirm` / `reject` |
| **머지 게이트** | `python -m jev_master code --state examples/risky.diff` | 디프: `merge` / `comment` / `block` |
| **화면 플레이그라운드** | `python -m jev_master browser` | 확률 막대, 포트 **8765** |
| **필드 목록** | `python -m jev_master catalog --kind vision` | 인용만. `--kind`는 아래 표 |

폴더: [`ticket_router`](apps/ticket_router) · [`confidence_gate`](apps/confidence_gate) · [`pitch_score`](apps/pitch_score) · [`jev_bot`](apps/jev_bot) · [`jev_harness`](apps/jev_harness) · [`jev_code`](apps/jev_code) · [`jev_browser`](apps/jev_browser)

단독 패키지: [jev-bot](https://github.com/kevin9327/jev-bot) · [jev-harness](https://github.com/kevin9327/jev-harness) · [jev-code](https://github.com/kevin9327/jev-code)

### B. 공개 필드 (382개, 클론 없음)

전체 표: [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md). 종류만 보려면:

| 종류 | 개수 | 내용 | 명령 | 전체 표 |
| --- | ---: | --- | --- | --- |
| `official` | 12 | TypeSafe 문서·SDK·게이트웨이 | `--kind official` | [공식](docs/ECOSYSTEM.md#official) |
| `sdk` | 40 | Python, JS, Go, Rust, Java 등 클라이언트 | `--kind sdk` | [SDK](docs/ECOSYSTEM.md#sdks-and-clients) |
| `agent` | 73 | MCP, 도구 게이트, 라우터, 압축 | `--kind agent` | [에이전트](docs/ECOSYSTEM.md#agents-gates-mcp) |
| `browser` | 32 | 브라우저·데스크톱·폰 컴퓨터 사용 | `--kind browser` | [브라우저](docs/ECOSYSTEM.md#browser-and-computer-use) |
| `vision` | 19 | 이미지: OCR→Jev, Djev, 로컬 VL | `--kind vision` | [비전](docs/ECOSYSTEM.md#vision-images-and-local-eyes) |
| `app` | 71 | 제품 (트리아지, SQL, 트레이딩 등) | `--kind app` | [앱](docs/ECOSYSTEM.md#applications) |
| `game` | 31 | Doom, 마리오, 스네이크, 드론 등 | `--kind game` | [게임](docs/ECOSYSTEM.md#games-and-simulations) |
| `research` | 58 | 로컬·오픈 Jev 복제 | `--kind research` | [복제](docs/ECOSYSTEM.md#open-replicas-and-evals) |
| `list` | 16 | 다른 awesome-jev 목록 | `--kind list` | [목록](docs/ECOSYSTEM.md#other-directories) |
| `x` | 30 | X 원글 | `--kind x` | [X](docs/ECOSYSTEM.md#x-threads) |

```bash
python -m jev_master catalog
python -m jev_master catalog --kind vision
python -m jev_master catalog --json
```

---

## 시작

1. Python 3.10+, [console.typesafe.ai/settings/keys](https://console.typesafe.ai/settings/keys)의 TypeSafe 키.
2. 클론, 테스트, **지금 연 셸**에 키. 커밋 금지. `.env` / `jevkey.txt`는 gitignore.
3. `ticket` 한 번 돌리고 `answers`(Jev)와 `decision`(이 저장소)을 구분해서 봅니다.

```bash
git clone https://github.com/kevin9327/jev-master
cd jev-master
python -m pip install -e ".[dev]"
python -m pytest
```

PowerShell: `$env:TYPESAFE_API_KEY = '…'` · bash: 같은 이름을 `export`. 그다음:

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt
```

## Jev가 돌려주는 것

한 호출에 세 종류를 섞고, 앱 결정은 코드가 만듭니다.

| 종류 | 묻는 것 | 받는 것 |
| --- | --- | --- |
| **Choice** | 이 중에 어느 쪽? | `choice`, `probabilities`, `confidence` |
| **Score** | 이 척도에서 어디? | `score`, `legend`, `probabilities`, `confidence` |
| **Noul** | 이게 참인가? | `noul` (`0`~`1`) |

```
state + questions  →  POST https://api.typesafe.ai/v1/systemone
                   →  여기 compose_*()  →  라우팅 / 게이트 / 점수
```

정책이 바뀌면 파이썬 계수를 바꿉니다. 프롬프트를 다시 쓰지 않습니다.

티켓 샘플 (`examples/stripe-ticket.txt`) 실제 호출:

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

테스트는 네트워크 없이 같은 모양의 답을 넣습니다.

## 화면

```bash
python -m jev_master browser
```

[http://127.0.0.1:8765](http://127.0.0.1:8765). 키는 서버 프로세스에만 있습니다.

## 이미지 (분류: `vision`)

**TypeSafe Jev는 텍스트만 봅니다.** X 직원: [wait a while](https://x.com/dotpem/status/2101335033609138382).

| 방법 | 모델이 보는 것 | 예 |
| --- | --- | --- |
| OCR / 캡션 | 글 | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) · [nothotdog](https://github.com/anishsrinivasan/nothotdog) |
| CV → JSON | 장면 숫자 | [jev-drone](https://github.com/RomanSlack/jev-drone) |
| 모델 교체 | 픽셀 | [djev-dev](https://github.com/Davipar/djev-dev) · [jev_local](https://github.com/Argos1111/jev_local) |
| 픽셀을 글로 | 격자 (그리기) | [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) |

Djev는 초대제입니다. TypeSafe 키는 거기서 401입니다. 목록: `python -m jev_master catalog --kind vision`

## 키

런타임에만 읽습니다. README·테스트·이슈·스크린샷에 키를 넣지 마세요.

## 안 될 때

| 증상 | 볼 곳 |
| --- | --- |
| `TYPESAFE_API_KEY is not set` | **지금 연 셸**에 키 |
| HTTP 401 | TypeSafe 키 → `api.typesafe.ai`. Djev는 `djev_invite_…` |
| HTTP 403 | TypeSafe 대기열 |
| Windows `pip install -e .` 실패 | Python 3.10+. 테스트는 `PYTHONPATH=src` 후 `python -m pytest` |
| 브라우저 빈 화면 | 먼저 `browser` 실행, 그다음 8765 |
| `--kind` 오류 | **B** 표의 종류 이름만 |

## 라이선스

MIT. [LICENSE](LICENSE).

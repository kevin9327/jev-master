<p align="center">
  <img src="docs/assets/live-run.png" alt="실제 Jev 호출: POST /v1/systemone, Choice + Score + Noul" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/model-jev--latest-14b8a6" alt="jev-latest">
  <img src="https://img.shields.io/badge/POST-/v1/systemone-0f766e" alt="System One">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-5eead4" alt="MIT">
  <img src="https://img.shields.io/badge/catalog-382_citations-134e4a" alt="인용 382">
</p>

<p align="center"><b>상태를 넣고, 타입이 있는 답을 받고, 분기는 코드가 합니다.</b></p>

# jev-master

[TypeSafe Jev](https://docs.typesafe.ai/concepts/system-one)를 실제로 돌리는 작은 파이썬 모노레포입니다. 앱, `POST /v1/systemone` 클라이언트, 공개 프로젝트 인용 목록이 들어 있습니다.

Jev는 챗봇이 아닙니다. **판단할 내용(state)** 과 **질문(questions)** 을 보내면, 프로그램이 바로 갈라질 수 있는 확률을 돌려줍니다. 이 저장소는 생성된 글을 파싱하지 않습니다.

위 화면은 `examples/stripe-ticket.txt`에 대한 실제 `jev-1.13.0` 호출입니다. 부서 `billing`(0.69), 불만 `1.0`, 긴급 `0.99` → `act` / `billing_priority_queue`. 원본 JSON: [`docs/assets/live-run.json`](docs/assets/live-run.json).

## 목차

- [이 저장소가 하는 일](#이-저장소가-하는-일)
- [Jev가 돌려주는 것](#jev가-돌려주는-것)
- [바로 실행](#바로-실행)
- [앱을 고르는 법](#앱을-고르는-법)
- [출력 예](#출력-예)
- [브라우저](#브라우저)
- [이미지 (공식 Jev는 사진을 못 봄)](#이미지-공식-jev는-사진을-못-봄)
- [필드맵](#필드맵)
- [키](#키)
- [안 될 때](#안-될-때)
- [라이선스](#라이선스)

## 이 저장소가 하는 일

| | 역할 |
| --- | --- |
| **이 저장소** | 실행 가능한 조합 로직 + 테스트 + 인용 목록 |
| **TypeSafe Jev** | 호스트된 **텍스트** 판단 모델 (`api.typesafe.ai`) |
| **Djev** | 이미지가 되는 Maisa 프리뷰 ([djev.dev](https://djev.dev)) — TypeSafe가 아님 |
| **awesome-jev** | 링크 모음. 코드는 없음 |

TypeSafe와 무관합니다. 벤더가 적은 속도·가격은 벤더 숫자입니다.

## Jev가 돌려주는 것

한 번의 HTTP 호출에 세 종류를 섞을 수 있습니다.

| 종류 | 묻는 것 | 받는 것 |
| --- | --- | --- |
| **Choice** | 이 중에 어느 쪽? | `choice`, `probabilities`, `confidence` |
| **Score** | 이 척도에서 어디? | `score`, `legend`, `probabilities`, `confidence` |
| **Noul** | 이게 참인가? | `noul` (`0`~`1`) |

```
state + questions  →  POST https://api.typesafe.ai/v1/systemone
                      타입이 있는 답 (문장 없음)
                   →  이 저장소의 compose_*()
                   →  라우팅 / 게이트 / 점수
```

정책이 바뀌면 파이썬 계수를 바꿉니다. 프롬프트를 다시 쓰지 않습니다.

## 바로 실행

**필요:** Python 3.10+, [console.typesafe.ai/settings/keys](https://console.typesafe.ai/settings/keys)에서 받은 TypeSafe 키.

키는 커밋하지 마세요. 환경 변수로 두거나 저장소 밖에 둡니다. `.env`, `jevkey.txt`는 gitignore되어 있습니다.

```bash
git clone https://github.com/kevin9327/jev-master
cd jev-master
python -m pip install -e ".[dev]"
python -m pytest
```

지금 연 셸에 `TYPESAFE_API_KEY`를 넣습니다. PowerShell은 `$env:TYPESAFE_API_KEY = '…'`, bash는 같은 이름을 `export` 합니다. 그다음:

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt
```

JSON에 Jev의 `answers`와 이 저장소가 만든 `decision`이 같이 나와야 합니다.

## 앱을 고르는 법

| 명령 | 이럴 때 | 코드가 만드는 결과 |
| --- | --- | --- |
| `python -m jev_master ticket --state examples/stripe-ticket.txt` | 문의 부서·대기열 | 부서 + `act`/`escalate` + 핸들러 |
| `python -m jev_master gate --state examples/voice-command.txt` | 위험한 동작, 확신 문턱 | `act` / `confirm` / `escalate` |
| `python -m jev_master pitch --state examples/pitch.txt` | 라벨 하나가 아니라 가중합 | 0~1 점수 + 판정 |
| `python -m jev_master bot --state examples/stripe-ticket.txt` | 고정 답변 (채팅 LLM 아님) | `reply` / `escalate` / `block` |
| `python -m jev_master harness --state examples/rm-step.json` | 에이전트가 도구를 쓰려 할 때 | `execute` / `confirm` / `reject` |
| `python -m jev_master code --state examples/risky.diff` | 디프 머지 게이트 | `merge` / `comment` / `block` |
| `python -m jev_master browser` | 확률을 화면으로 볼 때 | 같은 조합기, 포트 **8765** |
| `python -m jev_master catalog` | 인용된 382개 프로젝트 | 링크만, 클론 없음 |
| `python -m jev_master catalog --kind vision` | 이미지 관련만 | Djev, OCR 후 Jev, 로컬 VL |

같은 아이디어의 단독 패키지: [jev-bot](https://github.com/kevin9327/jev-bot) · [jev-harness](https://github.com/kevin9327/jev-harness) · [jev-code](https://github.com/kevin9327/jev-code)

앱 폴더 README: [`apps/ticket_router`](apps/ticket_router) · [`apps/confidence_gate`](apps/confidence_gate) · [`apps/pitch_score`](apps/pitch_score) · [`apps/jev_bot`](apps/jev_bot) · [`apps/jev_harness`](apps/jev_harness) · [`apps/jev_code`](apps/jev_code) · [`apps/jev_browser`](apps/jev_browser)

## 출력 예

티켓 샘플 (`examples/stripe-ticket.txt`):

```text
Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.
```

실제 호출(줄임):

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

`answers`는 Jev, `decision`은 여기 코드입니다. 테스트는 네트워크 없이 같은 모양의 답을 넣습니다 (`jev_master.client`와 `compose_*()`가 분리되어 있습니다).

## 브라우저

```bash
python -m jev_master browser
```

[http://127.0.0.1:8765](http://127.0.0.1:8765) 를 엽니다. 페이지는 같은 조합기를 씁니다. API 키는 서버 프로세스에만 있고 브라우저 번들에는 없습니다.

## 이미지 (공식 Jev는 사진을 못 봄)

TypeSafe 문서: **텍스트/JSON만**. X에서 TypeSafe 직원은 [wait a while](https://x.com/dotpem/status/2101335033609138382)이라고 했습니다.

그래도 “이미지 판단”을 하는 공개 작업은 아래 네 갈래입니다. **이 트리에 클론하지 않았습니다.** 인용만 합니다.

| 방법 | 판단 모델이 실제로 보는 것 | 예 |
| --- | --- | --- |
| OCR / 캡션 | 글 | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) · [nothotdog](https://github.com/anishsrinivasan/nothotdog) |
| CV → JSON | 장면 숫자 | [jev-drone](https://github.com/RomanSlack/jev-drone) |
| 모델 교체 | 픽셀 | [djev-dev](https://github.com/Davipar/djev-dev) · [jev_local](https://github.com/Argos1111/jev_local) · [jev-visual](https://github.com/hr98w/jev-visual) |
| 픽셀을 글로 물어봄 | 격자 (그리기, 보기 아님) | [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) |

[Djev](https://djev.dev)는 **Maisa** 초대제 프리뷰입니다. `TYPESAFE_API_KEY`로는 안 됩니다.

```bash
python -m jev_master catalog --kind vision
```

## 필드맵

2026-09-20 기준 GitHub/X 인용 **382개**. **링크만** 있습니다. 서브모듈·vendor 폴더는 없습니다.

```bash
python -m jev_master catalog                 # 전체
python -m jev_master catalog --kind browser  # 브라우저·컴퓨터 사용
python -m jev_master catalog --kind vision   # 이미지
python -m jev_master catalog --json          # JSON
```

종류: `official` `sdk` `agent` `browser` `vision` `app` `game` `research` `list` `x`

- 표: [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md)
- JSON: [`docs/ecosystem.json`](docs/ecosystem.json)

대표 인용: [python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) · [JS SDK](https://github.com/typesafe-ai/typesafe-sdk-js) · [skills](https://github.com/typesafe-ai/skills) · [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [djev-dev](https://github.com/Davipar/djev-dev) · [awesome-jev](https://github.com/cobanov/awesome-jev)

TypeSafe: [소개](https://docs.typesafe.ai/introduction) · [API](https://docs.typesafe.ai/api) · [패턴](https://docs.typesafe.ai/patterns)

## 키

런타임에만 읽습니다. README, 테스트, 이슈, 스크린샷에 키를 넣지 마세요.

## 안 될 때

| 증상 | 볼 곳 |
| --- | --- |
| `TYPESAFE_API_KEY is not set` | **지금 연 셸**에 환경 변수를 넣고 다시 실행 |
| HTTP 401 | 제품이 다름. TypeSafe 키 → `api.typesafe.ai`. Djev는 `djev_invite_…` |
| HTTP 403 / waitlist | 키는 있는데 TypeSafe 계정이 아직 안 열린 경우 |
| Windows에서 `pip install -e .` 실패 | Python 3.10+ 확인. 테스트는 `PYTHONPATH=src` 로 `python -m pytest` |
| 브라우저가 비어 있음 | 먼저 `python -m jev_master browser` 를 켠 뒤 8765 |
| catalog `--kind` 오류 | 위에 적은 종류 이름만 가능 |

## 라이선스

MIT. [LICENSE](LICENSE).

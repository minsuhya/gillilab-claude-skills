---
name: biz-idea-lab
description: >
  트렌드 리서치, 아이디어 발굴, 타당성 분석, 비즈니스 모델 생성, 실행 로드맵까지
  창업 아이디어 발굴과 검증 전체 워크플로우를 수행한다.
  Scout 모드(정보 수집→패턴→아이디어 30개+→백로그)와
  Deep 모드(TOP5 선정→BMC→로드맵→액션 플랜)를 지원한다.
  "스타트업 아이디어", "사업 아이디어", "비즈니스 아이디어", "창업 아이디어",
  "비즈니스 모델 만들기", "비즈니스 모델 설계", "사업 기획", "트렌드 조사", "아이디어 발굴", "핫 스타트업",
  "인기 앱", "startup idea", "business idea", "idea scout", "아이디어 스카우트",
  "business model" 등의 키워드로 트리거.
---

# Biz Idea Lab

트렌드 스캔부터 실행 가능한 비즈니스 모델까지, 체계적 워크플로우로 창업 아이디어를 발굴·검증한다.

## 모드 선택

| 모드 | 범위 | 출력 |
|------|------|------|
| **Scout** | Phase 1-3 | 아이디어 백로그 (30개+) + TOP Pick 카드 |
| **Deep** | Phase 1-6 | BMC + 로드맵 + 액션 플랜 (전체 분석) |

AskUserQuestion으로 모드와 컨텍스트를 수집한다:

1. **모드**: Scout (발굴만) / Deep (전체 분석)
2. **관심 도메인** (멀티셀렉): IT/SaaS, 이커머스, 헬스케어, 핀테크, 에듀테크, 전체
3. **타겟 시장**: 한국 집중 / 글로벌+한국 / 글로벌
4. **보유 기술/도메인**: IT, 이커머스/유통, 제조, 서비스업, 기타
5. **초기 투자 규모**: 부트스트랩(<1억), 소규모(1-5억), 시드(5-30억), 시리즈A
6. **팀 구성**: 1인 창업자, 공동창업자, 기존 팀

## Phase 1: 트렌드 리서치 (병렬 6채널)

| 채널 | 출력 파일 | 핵심 내용 |
|------|-----------|-----------|
| 글로벌 테크 트렌드 | `01-signals/trends.md` | Product Hunt, HN, GitHub Trending |
| 핫 스타트업 & 펀딩 | `01-signals/startups.md` | TechCrunch, YC 배치 |
| 신규 인기 앱 | `01-signals/apps.md` | App Store/Play 차트 |
| VC 투자 동향 | `01-signals/investments.md` | CB Insights, VC 포트폴리오 |
| 커뮤니티 신호 | `01-signals/communities.md` | Reddit, Indie Hackers |
| 한국 시장 특화 | `01-signals/korea-market.md` | 벤처스퀘어, 국내 앱 트렌드 |

정보 원천 상세: [references/global-sources.md](references/global-sources.md), [references/korea-sources.md](references/korea-sources.md)

## Phase 2: 패턴 인식 → 아이디어 생성

### 패턴 추출 (`02-patterns/pattern-analysis.md`)

6개 채널 신호를 교차 분석: 반복 Pain Point, 기술 신호 수렴, 급성장 카테고리, 시장 갭, 크로스 도메인 기회, 한국 특화 기회

### 아이디어 생성 (30개+, `03-ideas/idea-backlog.md`)

5가지 렌즈로 도출:
1. **Pain → Product**: 발견된 Pain Point 직접 해결
2. **Technology → Application**: 급성장 기술의 새 도메인 적용
3. **Copy → Localize**: 해외 성공 모델 한국 현지화
4. **Vertical → Horizontal**: 산업 특화 → 범용 플랫폼
5. **Offline → Online**: 오프라인 프로세스 디지털화

30개 미달 시 5가지 렌즈를 추가 적용하거나 관심 도메인 범위를 확장한 후 재도출한다.

백로그 템플릿: [references/idea-backlog-template.md](references/idea-backlog-template.md)

## Phase 3: 스코어링 & TOP Pick

### 빠른 스코어링 (15점 만점)

| 기준 | 5점 | 3점 | 1점 |
|------|-----|-----|-----|
| 시장 크기 | TAM > 1조 | 100억~1조 | 100억 미만 |
| 구현 가능성 | 6개월 내 MVP | 1-2년 | 미정 |
| 차별화 | AI/기술 해자 명확 | 부분적 | 레드오션 |

- 12-15점: TOP Pick → 상세 카드 (`04-top-picks/`)
- 9-11점: 관심 아이디어 (재검토 대상)
- 8점 이하: 참고/보관

**Scout 모드는 여기서 종료.** README 요약 생성 후 다음 단계 안내.
Scout 완료 후 Deep 전환 요청 시 기존 출력을 그대로 이어 Phase 4부터 진행한다.

사용자 확인: "TOP3 추천: {A}, {B}, {C}. Deep 분석 진행할까요?"

## Phase 4: 비즈니스 모델 캔버스 (Deep 모드, TOP3)

TOP3에 대해 BMC 9블록 + 재무 예측 + BEP + 투자 계획을 작성한다.

평가 매트릭스: [references/evaluation-matrix-template.md](references/evaluation-matrix-template.md)
BMC 템플릿: [references/bmc-template.md](references/bmc-template.md)

출력: `05-business-models/bmc-0{N}-{name}.md` (3개)

## Phase 5: 실행 로드맵 (Deep 모드)

포함: 전략 개요, 월간 계획, 팀 구성 로드맵, 핵심 KPI, 투자 로드맵, 리스크 & 컨틴전시

로드맵 템플릿: [references/roadmap-template.md](references/roadmap-template.md)

출력: `06-roadmap/execution-roadmap.md`

## Phase 6: 액션 플랜 + README (Deep 모드)

포함: 이번 주/월/3개월/6개월 체크리스트, 핵심 가설 검증 계획, 리스크 모니터링

액션 플랜 템플릿: [references/action-plan-template.md](references/action-plan-template.md)

출력: `07-next-steps/action-plan.md` + `README.md`

## 출력 디렉터리

출력 디렉터리는 사용자 지정 경로 또는 현재 작업 디렉터리에 생성한다.
출력 디렉터리가 이미 존재하는 경우 사용자에게 덮어쓰기 여부를 확인한다.

```
biz-idea-lab/
├── README.md
├── 01-signals/          # 채널별 수집 신호
├── 02-patterns/         # 패턴 분석
├── 03-ideas/            # 아이디어 백로그
├── 04-top-picks/        # TOP 상세 카드
├── 05-business-models/  # BMC TOP3 (Deep)
├── 06-roadmap/          # 실행 로드맵 (Deep)
└── 07-next-steps/       # 액션 플랜 (Deep)
```

## 사용자 확인 포인트

- Phase 1 완료: "리서치 완성. 아이디어 발굴로 진행할까요?"
- Phase 2 완료: "패턴 분석 완성. 아이디어 30개+ 생성으로 진행할까요?"
- Phase 3 완료: "TOP3 추천: {A}, {B}, {C}. BMC 생성 진행할까요?"
- Phase 4 완료: "BMC 완성. 실행 로드맵 작성 진행할까요?"

## 스킬 연동

확정 아이디어 → `/project-builder`로 서비스 문서화 및 앱 구현 진행

## 웹 검색 환경 처리

| 환경 | 처리 방식 |
|------|---------|
| 웹 검색 가능 | 실시간 데이터 우선, 최신 3-6개월 기준 |
| 웹 검색 불가 | 학습 데이터 기반 분석 (2024-2025년 데이터) |

- 웹 검색 불가 시 모든 수치에 `[추정: {근거}]` 태그를 붙인다
- 실시간 검증이 필요한 항목에는 `[실시간 검증 필요]` 태그를 사용한다
- 사용자에게 웹 검색 가능 환경 구성을 권장한다

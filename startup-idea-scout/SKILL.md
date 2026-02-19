---
name: startup-idea-scout
description: |
  다양한 정보 원천(트렌드, 핫 스타트업, 신규 인기앱, VC 투자 동향, SNS, 커뮤니티)을 체계적으로
  스캔하여 스타트업 사업 아이디어를 발굴·수집·정리하는 스킬.
  수집된 아이디어를 구조화된 백로그로 정리하고 빠른 초기 스코어링까지 수행합니다.
  business-idea-generator 스킬의 선행 단계로 활용 가능합니다.
triggers:
  - "스타트업 아이디어"
  - "사업 아이디어 수집"
  - "트렌드 조사"
  - "아이디어 발굴"
  - "핫 스타트업"
  - "인기 앱"
  - "startup idea"
  - "idea scout"
  - "startup-idea-scout"
  - "아이디어 스카우트"
---

# Startup Idea Scout 스킬

## 개요

**"좋은 아이디어는 좋은 정보에서 나온다"**

트렌드, 핫 스타트업, 신규 인기 앱, VC 투자 동향, SNS, 개발자 커뮤니티 등 **10개+ 정보 원천**을
병렬로 스캔하여 스타트업 사업 아이디어를 체계적으로 발굴합니다.

```
Phase 1: 정보 원천 설정     → 타겟 도메인 & 스캔 범위 설정
Phase 2: 병렬 정보 수집     → 10개+ 채널 동시 스캔 (ultrawork)
Phase 3: 패턴 인식          → 반복 등장 키워드·문제·기술 추출
Phase 4: 아이디어 생성      → 수집된 신호 기반 아이디어 도출
Phase 5: 백로그 구조화      → 스코어링 + 카테고리별 정리
Phase 6: 리포트 생성        → 실행 가능한 아이디어 백로그 출력
```

---

## 실행 방법

```bash
/startup-idea-scout
```

옵션:
```bash
/startup-idea-scout --domain "헬스케어"          # 특정 도메인 집중 스캔
/startup-idea-scout --region "korea"             # 한국 시장 집중 (기본값)
/startup-idea-scout --region "global"            # 글로벌 시장
/startup-idea-scout --depth "quick"              # 빠른 스캔 (2-3개 소스)
/startup-idea-scout --depth "deep"               # 심층 스캔 (모든 소스, 기본값)
/startup-idea-scout --output-dir "idea-backlog"  # 출력 디렉토리 지정
/startup-idea-scout --top 20                     # 상위 N개 아이디어 (기본: 30)
```

---

## Phase 0: 초기 설정

### 0.1 출력 디렉토리 생성

```
{output-dir}/                          # 기본: idea-backlog/
├── README.md                          # 전체 스캔 결과 요약
├── 01-signals/                        # 수집된 원시 신호들
│   ├── trends.md                      # 트렌드 신호
│   ├── startups.md                    # 스타트업 신호
│   ├── apps.md                        # 앱 신호
│   ├── investments.md                 # 투자 신호
│   ├── communities.md                 # 커뮤니티 신호
│   └── korea-market.md               # 한국 시장 신호
├── 02-patterns/                       # 패턴 분석 결과
│   └── pattern-analysis.md
├── 03-ideas/                          # 도출된 아이디어
│   └── idea-backlog.md               # 전체 아이디어 백로그
└── 04-top-picks/                      # TOP 아이디어 상세
    ├── pick-01-{name}.md
    ├── pick-02-{name}.md
    └── pick-03-{name}.md
```

### 0.2 스캔 설정 (AskUserQuestion 사용)

**질문 1**: 관심 도메인 (멀티셀렉 가능)
- IT/SaaS, 이커머스/리테일, 헬스케어, 핀테크, 에듀테크
- 푸드테크, 물류/모빌리티, B2B 엔터프라이즈, 컨슈머/라이프스타일, 전체

**질문 2**: 스캔 깊이
- Quick (주요 소스 3-5개, 15분), Deep (전체 소스 10개+, 45분)

**질문 3**: 타겟 시장
- 한국 집중, 글로벌 레퍼런스 + 한국 적용, 글로벌 전체

---

## Phase 1: 병렬 정보 수집 [ULTRAWORK 활성화]

### 채널 A: 글로벌 테크 트렌드

**정보 원천 및 스캔 키워드**:

```
Product Hunt (producthunt.com)
  - 검색: "trending today", "top products this week"
  - 추출: 카테고리별 상위 제품, upvote 수, 문제 설명

Hacker News (news.ycombinator.com)
  - 검색: "Show HN", "Ask HN: who is hiring", "new startup"
  - 추출: 반복 등장 기술, 창업자 고통 포인트

GitHub Trending (github.com/trending)
  - 검색: trending repositories (1주일/1개월)
  - 추출: 급성장 기술, 개발자 관심사

a16z / Sequoia 블로그
  - 검색: "investment thesis 2025 2026", "market maps"
  - 추출: VC가 베팅하는 섹터, 신기술 카테고리
```

**출력** → `01-signals/trends.md`

```markdown
## 글로벌 테크 트렌드 신호

### Product Hunt TOP 신호
| 제품명 | 카테고리 | 핵심 문제 | Upvotes |
|--------|---------|---------|--------|

### Hacker News 반복 키워드
- {KEYWORD_1}: {CONTEXT}
- {KEYWORD_2}: {CONTEXT}

### GitHub 급성장 기술
- {TECH_1}: {DESCRIPTION}
- {TECH_2}: {DESCRIPTION}

### VC 투자 테마 (a16z/Sequoia)
- {THEME_1}: {DESCRIPTION}
```

---

### 채널 B: 핫 스타트업 & 펀딩 동향

**정보 원천**:

```
TechCrunch (techcrunch.com)
  - 검색: "raises", "seed round", "series A" + 최근 3개월
  - 추출: 펀딩받은 스타트업, 해결 문제, 투자액

Crunchbase / AngelList 트렌드
  - 검색: 최근 시드/시리즈A 투자 기업
  - 추출: 카테고리별 펀딩 트렌드

Y Combinator 최신 배치
  - 검색: "YC W25", "YC S25" (최신 배치)
  - 추출: 배치 기업 목록, 해결 문제, 초기 트랙션

한국 스타트업 (한국 시장 시)
  - 벤처스퀘어, platum, 아웃스탠딩
  - 검색: 최근 투자 유치 스타트업
  - 추출: 카테고리, 문제, 투자액
```

**출력** → `01-signals/startups.md`

```markdown
## 핫 스타트업 신호

### 글로벌 최근 펀딩 스타트업 (최근 3개월)
| 스타트업 | 카테고리 | 해결 문제 | 펀딩 | 투자사 |
|---------|---------|---------|------|-------|

### YC 최신 배치 주목 기업
| 기업명 | 한 줄 설명 | 초기 트랙션 |
|--------|---------|-----------|

### 한국 최근 투자 유치 스타트업
| 기업명 | 카테고리 | 투자액 | 투자사 |
|--------|---------|-------|-------|
```

---

### 채널 C: 신규 인기 앱 & 소비자 트렌드

**정보 원천**:

```
App Store / Google Play 트렌딩
  - iOS/Android 카테고리별 TOP 차트
  - 검색: 신규 진입 앱 (3개월 내 출시)
  - 추출: 급상승 앱, 리뷰 수, 해결 기능

Sensor Tower / AppFollow 데이터
  - 검색: "breakout apps 2025 2026"
  - 추출: 다운로드 급증 앱

소셜 미디어 바이럴 앱
  - TikTok/인스타그램에서 바이럴된 앱
  - 검색: "this app", "use this app" 트렌드
  - 추출: 바이럴 이유, 핵심 기능

한국 앱 마켓 (한국 시장 시)
  - 네이버 앱스토어, 원스토어 트렌딩
  - 카카오 인기 서비스 신규 기능
```

**출력** → `01-signals/apps.md`

```markdown
## 신규 인기 앱 신호

### App Store / Google Play 급상승
| 앱 이름 | 카테고리 | 핵심 기능 | 출시일 | 특징 |
|--------|---------|---------|------|-----|

### 소셜 바이럴 앱
| 앱 이름 | 바이럴 플랫폼 | 핵심 기능 | 왜 바이럴됐나 |
|--------|------------|---------|------------|

### 리뷰 급증 앱 (문제 단서)
앱 리뷰에서 반복 등장하는 불만/요청:
- "{COMPLAINT_1}" → 기회: {OPPORTUNITY}
- "{COMPLAINT_2}" → 기회: {OPPORTUNITY}
```

---

### 채널 D: VC & 투자 동향 분석

**정보 원천**:

```
CB Insights 보고서
  - 검색: "state of venture 2025 2026", "emerging sectors"
  - 추출: 섹터별 투자 증감, 유니콘 예비 기업

Pitchbook 트렌드
  - 검색: "most funded categories 2025"
  - 추출: 핫 카테고리, 평균 밸류에이션

주요 VC 투자 포트폴리오
  - a16z, Sequoia, Bessemer, Andreessen 최신 포트폴리오
  - 소프트뱅크, 카카오벤처스, 한국투자파트너스 (한국 시장)
  - 추출: 신규 투자 기업, 테마

AI 관련 투자 집중 분석
  - 검색: "AI startup funding 2026"
  - 추출: AI 적용 분야별 투자 규모
```

**출력** → `01-signals/investments.md`

```markdown
## 투자 동향 신호

### 섹터별 투자 증감 (최근 6개월)
| 섹터 | 투자 방향 | 주목 이유 |
|------|---------|---------|
| {SECTOR_1} | ↑ 증가 | {REASON} |

### 주요 VC 최신 투자 테마
| VC | 투자 테마 | 대표 포트폴리오 |
|----|---------|-------------|

### AI 투자 집중 분야
- {AI_DOMAIN_1}: {INVESTMENT_SIGNAL}
- {AI_DOMAIN_2}: {INVESTMENT_SIGNAL}
```

---

### 채널 E: 개발자 & 테크 커뮤니티 신호

**정보 원천**:

```
Reddit (reddit.com)
  - r/startups, r/SaaS, r/entrepreneur, r/ChatGPT, r/artificial
  - 검색: "I built", "I made", "validate my idea"
  - 추출: 직접 만든 프로젝트, 고통 포인트

Twitter/X 테크 커뮤니티
  - 검색: "just launched", "we built", "show your startup"
  - 인디 해커, 메이커 커뮤니티 트윗
  - 추출: 인디 빌더 트렌드, 새 도구

Indie Hackers (indiehackers.com)
  - 검색: 최근 수익 공개 사례, milestone 달성
  - 추출: 수익 내는 소규모 SaaS, 성공 패턴

한국 커뮤니티 (한국 시장 시)
  - GeekNews, 개발자 카카오 오픈채팅
  - 뽐뿌/클리앙 IT 게시판
  - 추출: 한국 개발자 고통 포인트, 자체 제작 도구
```

**출력** → `01-signals/communities.md`

```markdown
## 커뮤니티 신호

### Reddit "I built" 프로젝트 (최근 1개월)
| 프로젝트 | 해결 문제 | 반응 | 수익 |
|---------|---------|-----|-----|

### Indie Hackers 성공 패턴
| 제품 | MRR | 핵심 성공 요인 |
|-----|-----|------------|

### 개발자 커뮤니티 Pain Point
반복 등장하는 불만/요청:
- "{PAIN_1}": 등장 빈도 {N}회
- "{PAIN_2}": 등장 빈도 {N}회
```

---

### 채널 F: 한국 시장 특화 신호

**정보 원천**:

```
한국 스타트업 미디어
  - 벤처스퀘어 (venturesquare.net)
  - platum (platum.kr)
  - 아웃스탠딩 (outstanding.kr)
  - 검색: 최근 1개월 스타트업 소식

국내 앱 트렌드
  - 모바일인덱스, 앱애니 한국 데이터
  - 검색: "한국 앱 순위 2026", "국내 인기 앱"

한국 커머스 트렌드
  - 쿠팡, 네이버, 카카오 신규 서비스
  - 이커머스 박람회, COEX 전시회 소식
  - 검색: "한국 이커머스 트렌드 2026"

정부/공공 기회
  - 중소벤처기업부, KOTRA 지원 프로그램
  - K-스타트업 그랜드챌린지
  - 검색: "스타트업 정부지원 2026"

SNS 한국 트렌드
  - 인스타그램 한국 트렌딩 해시태그
  - 유튜브 급상승 (테크/비즈니스 카테고리)
  - 검색: "한국 스타트업 트렌드", "K-스타트업"
```

**출력** → `01-signals/korea-market.md`

```markdown
## 한국 시장 특화 신호

### 국내 스타트업 최신 소식
| 스타트업 | 카테고리 | 핵심 서비스 | 최근 소식 |
|---------|---------|----------|---------|

### 국내 앱 트렌드
| 앱 | 카테고리 | 성장 이유 |
|----|---------|---------|

### 한국 커머스 신규 서비스
| 서비스 | 제공사 | 타겟 | 기회 |
|--------|-------|-----|-----|

### 정부 지원 기회
| 프로그램 | 지원 내용 | 신청 자격 |
|---------|---------|---------|
```

---

## Phase 2: 패턴 인식 → `02-patterns/pattern-analysis.md`

수집된 6개 채널 신호를 교차 분석하여 패턴을 추출합니다.

### 패턴 분석 프레임워크

```markdown
## 패턴 분석 결과

### 1. 반복 등장 Pain Point (3개+ 채널에서 등장)
| Pain Point | 등장 채널 | 빈도 | 현재 솔루션의 한계 |
|-----------|---------|-----|----------------|

### 2. 기술 신호 수렴 (여러 소스에서 같은 기술 등장)
| 기술 | 등장 맥락 | 적용 가능 도메인 |
|-----|---------|--------------|

### 3. 급성장 카테고리 (투자 + 사용자 동시 증가)
| 카테고리 | 투자 신호 | 사용자 신호 | 한국 적용 가능성 |
|---------|---------|---------|-------------|

### 4. 시장 갭 (수요는 있으나 솔루션 부재)
| 갭 | 근거 | 예상 TAM |
|----|-----|--------|

### 5. 크로스 도메인 기회 (A분야 기술을 B분야에 적용)
| 원본 기술/모델 | 적용 도메인 | 기회 설명 |
|------------|---------|---------|

### 6. 한국 시장 특화 기회 (글로벌 트렌드 → 한국 적용)
| 글로벌 트렌드 | 한국 현황 | 기회 |
|------------|---------|-----|
```

---

## Phase 3: 아이디어 생성 → `03-ideas/idea-backlog.md`

패턴 분석을 기반으로 **최소 30개** 아이디어를 생성합니다.

### 아이디어 생성 프레임워크 (5가지 렌즈)

```
렌즈 1. Pain → Product
  발견된 Pain Point를 직접 해결하는 제품

렌즈 2. Technology → Application
  급성장 기술(AI, API)을 새 도메인에 적용

렌즈 3. Copy → Localize
  해외 성공 모델을 한국 시장에 맞게 현지화

렌즈 4. Vertical → Horizontal
  특정 산업 특화 솔루션 → 범용 플랫폼으로 확장

렌즈 5. Offline → Online
  오프라인 프로세스를 디지털화/자동화
```

### 아이디어 백로그 포맷

```markdown
## 아이디어 백로그 (총 {N}개)

### 카테고리: AI/SaaS

#### 아이디어 #001: {아이디어명}
- **한 줄 설명**: {DESCRIPTION}
- **해결 문제**: {PROBLEM}
- **타겟 고객**: {TARGET}
- **수익 모델**: {REVENUE_MODEL}
- **근거 신호**: {SOURCE_SIGNALS}  ← 어떤 정보에서 나왔는지
- **유사 사례**: {SIMILAR_PRODUCT}  ← 글로벌 유사 사례
- **빠른 스코어**: 시장 {M}/5 | 구현 {I}/5 | 차별화 {D}/5 | 합계 {TOTAL}/15

---

#### 아이디어 #002: {아이디어명}
...
```

### 카테고리 분류

- **AI/SaaS**: AI 기반 B2B 소프트웨어
- **이커머스/리테일**: 커머스 관련 솔루션
- **핀테크**: 금융/결제/보험
- **헬스케어**: 의료/웰니스/멘탈헬스
- **에듀테크**: 교육/학습/스킬업
- **크리에이터/콘텐츠**: 크리에이터 도구, 미디어
- **B2B 엔터프라이즈**: 기업용 솔루션
- **컨슈머/라이프스타일**: B2C 앱, 일상 솔루션
- **딥테크**: AI/로봇/바이오
- **기타/니치**: 특수 시장

---

## Phase 4: TOP 아이디어 상세 카드

스코어 상위 {TOP_N}개에 대해 상세 카드 작성 → `04-top-picks/pick-0{N}-{name}.md`

```markdown
# #{RANK}. {아이디어명}

**발굴 날짜**: {DATE}
**근거 채널**: {SOURCE_CHANNELS}
**빠른 스코어**: {SCORE}/15

---

## 핵심 인사이트
{WHY_THIS_IDEA_NOW}

## 문제 (Problem)
{DETAILED_PROBLEM}

**Pain Point 증거**:
- {EVIDENCE_1} (출처: {SOURCE})
- {EVIDENCE_2} (출처: {SOURCE})

## 솔루션 (Solution)
{SOLUTION_DESCRIPTION}

## 타겟 고객
{TARGET_CUSTOMER_PROFILE}

## 시장 크기 추정
- TAM: {TAM_ESTIMATE}
- 근거: {TAM_RATIONALE}

## 수익 모델
{REVENUE_MODEL}

## 유사/경쟁 사례
| 사례 | 시장 | 성과 | 차별화 포인트 |
|-----|-----|-----|------------|

## 구현 복잡도
- 기술 난이도: {LOW/MED/HIGH}
- 초기 팀 요구: {TEAM_REQUIREMENTS}
- 예상 MVP 기간: {MVP_TIMELINE}

## 리스크
- {RISK_1}
- {RISK_2}

## 다음 검증 단계
- [ ] {VALIDATION_STEP_1}
- [ ] {VALIDATION_STEP_2}

## 관련 아이디어 링크
- {RELATED_IDEA_1}
- {RELATED_IDEA_2}
```

---

## Phase 5: README 요약 생성 → `README.md`

```markdown
# 스타트업 아이디어 스카우트 리포트

**스캔 날짜**: {DATE}
**스캔 채널**: {N}개
**발굴 아이디어**: {TOTAL}개
**TOP 픽**: {TOP_N}개

## 핵심 발견사항

### 이번 스캔의 메가 트렌드
1. {MEGA_TREND_1}
2. {MEGA_TREND_2}
3. {MEGA_TREND_3}

### TOP {N} 아이디어 요약
| 순위 | 아이디어 | 카테고리 | 스코어 | 핵심 근거 |
|-----|---------|---------|-------|---------|

## 스캔 채널 요약
| 채널 | 수집 신호 수 | 주요 인사이트 |
|-----|-----------|-----------|

## 추천 다음 단계
이 아이디어들을 `/business-idea-generator` 스킬로 심층 분석하세요.
```

---

## 실행 원칙

### 정보 수집 전략

**웹 검색 가능 환경**:
```
- WebSearch로 각 채널 실시간 검색
- 최신 데이터 우선 (최근 3-6개월)
- 출처 명시 필수 (근거 신호 추적 가능하게)
```

**웹 검색 불가 환경**:
```
- 학습 데이터 기반 분석 (2024-2025년 데이터)
- "[추정]" 또는 "[학습 데이터 기준]" 태그 사용
- 검증이 필요한 항목에 "[실시간 검증 필요]" 표시
- 사용자에게 검색 가능 환경 구성 권장
```

### 빠른 스코어링 기준 (15점 만점)

| 기준 | 5점 | 3점 | 1점 |
|------|-----|-----|-----|
| **시장 크기** | TAM > 1조 | 100억~1조 | 100억 미만 |
| **구현 가능성** | 현재 기술로 6개월 | 1-2년 | 미정 |
| **차별화** | AI/기술 해자 명확 | 부분적 차별화 | 레드오션 |

스코어 기준:
- 12-15점: TOP Pick (즉시 심층 분석)
- 9-11점: 관심 아이디어 (다음 스캔 시 재검토)
- 6-8점: 참고 아이디어 (보관)
- 5점 이하: 제외

### 아이디어 업데이트 주기

```
주 1회 실행: 트렌드 신호 업데이트
월 1회 실행: 전체 채널 심층 스캔
분기 1회: 백로그 정리 + business-idea-generator로 TOP3 심층 분석
```

---

## 스킬 연동 워크플로우

```
startup-idea-scout (이 스킬)
        ↓
  아이디어 백로그 생성 (30개+)
        ↓
  TOP 3-5 선정
        ↓
/business-idea-generator --skip-research
(이미 수집된 아이디어를 BMC + 로드맵으로 발전)
        ↓
/service-docs-generator
(확정된 아이디어를 실제 서비스 문서로)
        ↓
/idea-to-app
(서비스를 실제 앱으로 구현)
```

---

## 관련 스킬

- `/business-idea-generator` - 아이디어를 BMC + 로드맵으로 발전
- `/it-news-collector` - IT 뉴스 특화 수집
- `/service-docs-generator` - 선정 아이디어 서비스 문서화

---

*이 스킬은 정기적으로 실행하여 아이디어 백로그를 지속 업데이트하세요.*
*좋은 아이디어는 한 번의 스캔이 아니라 지속적인 관찰에서 나옵니다.*

# 사용 예시

## 예시 1: 학습 플랫폼 (Project Lattice)

### 사용자 요청

```
캘린더 기반 학습 계획 + AI 콘텐츠 생성 플랫폼을 만들려고 해.
프로젝트 문서화 해줘.
```

### 정보 수집 대화

```
Claude: 서비스 문서화를 시작하겠습니다. 몇 가지 정보가 필요합니다.

1. 프로젝트명 (내부 코드명)?
User: Project Lattice

2. 서비스명 (브랜드명)?
User: 캘리런 (CaliLearn)

3. 타겟 사용자는 누구인가요?
User: 1차: 고등학생 (내신/수능), 확장: 자기계발 학습자

4. 기술 스택 선호도가 있나요?
User: React, FastAPI, Expo (모바일)

5. MVP에서 꼭 필요한 기능은?
User: 계획 자동 생성, 캘린더 뷰, AI 콘텐츠, 알림
```

### 생성 결과

```
lattice/
├── CLAUDE.md
├── README.md
├── .cursorrules
└── docs/
    ├── 01-prd.md
    ├── 02-architecture.md
    ├── 03-content-strategy.md
    ├── 04-api-spec.md
    ├── 05-roadmap.md
    ├── 06-dev-guide.md
    ├── 07-mvp-checklist.md
    └── policies/
        ├── planning-policy.md
        ├── notification-policy.md
        └── replan-policy.md
```

---

## 예시 2: 실시간 채팅 서비스

### 사용자 요청

```
실시간 고객 상담 채팅 서비스를 만들려고 해. 문서화 해줘.
```

### 정보 수집 대화

```
Claude: 서비스 문서화를 시작하겠습니다.

1. 프로젝트명?
User: Project Helios

2. 서비스명?
User: 헬프챗 (HelpChat)

3. 타겟 사용자?
User: 중소기업 고객센터

4. 핵심 기능?
User: 실시간 채팅, 상담원 배정, 대화 기록, 통계

5. 기술 스택?
User: Next.js, Socket.io, PostgreSQL
```

### 생성 결과

```
helios/
├── CLAUDE.md
├── README.md
├── .cursorrules
└── docs/
    ├── 01-prd.md
    ├── 02-architecture.md
    ├── 03-realtime-strategy.md      # 도메인별 전략
    ├── 04-api-spec.md
    ├── 05-roadmap.md
    ├── 06-dev-guide.md
    ├── 07-mvp-checklist.md
    └── policies/
        ├── routing-policy.md         # 상담원 배정 정책
        └── escalation-policy.md      # 에스컬레이션 정책
```

---

## 예시 3: 커머스 플랫폼

### 사용자 요청

```
핸드메이드 제품 마켓플레이스를 만들어야 해.
```

### 정보 수집 후 생성 결과

```
marketplace/
├── CLAUDE.md
├── README.md
├── .cursorrules
└── docs/
    ├── 01-prd.md
    ├── 02-architecture.md
    ├── 03-commerce-strategy.md      # 커머스 전략
    ├── 04-api-spec.md
    ├── 05-roadmap.md
    ├── 06-dev-guide.md
    ├── 07-mvp-checklist.md
    └── policies/
        ├── pricing-policy.md         # 가격/수수료 정책
        ├── refund-policy.md          # 환불 정책
        └── seller-policy.md          # 판매자 정책
```

---

## 도메인별 전략 문서 예시

### AI 서비스 → 03-ai-strategy.md

```markdown
# AI 전략

## 1. 생성 전략
- 선생성 vs 온디맨드
- 모델 선택 (Local/Cloud)
- 프롬프트 관리

## 2. 품질 검증
- 자동 검증 규칙
- 휴먼 인더 루프

## 3. 비용 최적화
- 캐싱 전략
- 배치 처리
```

### 실시간 서비스 → 03-realtime-strategy.md

```markdown
# 실시간 전략

## 1. 연결 관리
- WebSocket vs SSE
- 재연결 정책

## 2. 메시지 처리
- 순서 보장
- 중복 방지

## 3. 확장성
- 수평 확장
- 로드 밸런싱
```

### 커머스 → 03-commerce-strategy.md

```markdown
# 커머스 전략

## 1. 결제
- 결제 수단
- 정산 주기

## 2. 배송
- 배송 추적
- 반품 처리

## 3. 재고
- 재고 관리
- 품절 처리
```

---

## 정책 문서 예시

### planning-policy.md (학습 계획 정책)

```markdown
# 학습 계획 정책

## 핵심 상수

| 상수 | 값 | 설명 |
|------|-----|------|
| MAX_DAILY_MINUTES | 180 | 최대 일일 학습 시간 |
| DEFAULT_DAILY_MINUTES | 60 | 기본 일일 학습 시간 |

## 생성 규칙

1. 학습 가능 요일만 할당
2. 일일 시간 내에서 분배
3. 난이도 순차적 증가

## 재계획 트리거

- 연속 2일 미이행
- 사용자 명시적 요청
```

### routing-policy.md (상담원 배정 정책)

```markdown
# 상담원 배정 정책

## 배정 알고리즘

1. 스킬 매칭 (필수)
2. 현재 상담 수 (우선순위)
3. 라운드 로빈 (동일 조건시)

## 에스컬레이션

- 5분 무응답 → 다른 상담원
- 고객 요청 → 슈퍼바이저

## 업무 시간 외

- 챗봇 응대
- 티켓 생성
```

---

## 바이브 코딩 워크플로우

스킬로 문서 생성 후 개발 시작:

```
1. 문서 생성 완료
   ↓
2. docs/07-mvp-checklist.md 확인
   ↓
3. Phase 1부터 순차 진행
   ↓
4. "Phase 1 시작해줘" 요청
   ↓
5. Claude가 체크리스트 기반 구현
   ↓
6. Phase 완료 → 다음 Phase
```

### 대화 예시

```
User: Phase 1 시작해줘

Claude: docs/07-mvp-checklist.md의 Phase 1을 확인했습니다.

Phase 1: 프로젝트 초기화
- [ ] 모노레포 구조 생성
- [ ] 패키지 의존성 설정
- [ ] 개발 환경 설정

순서대로 진행하겠습니다. 먼저 모노레포 구조를 생성합니다...
```

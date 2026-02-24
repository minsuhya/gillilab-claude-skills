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


---

# idea-to-app 사용 예시

이 파일은 idea-to-app 스킬의 실제 사용 예시를 보여줍니다.

---

## 예시 1: 코드 리뷰 자동화 플랫폼

### 1.1 IDEA.md

```markdown
# CodeReview AI

## 한 줄 소개
개발자를 위한 AI 기반 코드 리뷰 자동화 플랫폼

## 핵심 가치
- 코드 품질을 자동으로 검증하여 리뷰 시간을 50% 단축
- AI가 보안 취약점을 사전에 탐지
- 팀의 코딩 컨벤션을 자동으로 학습하고 적용

## 타겟 사용자
- 주 타겟: 스타트업 및 중소기업의 개발 팀 (3-10명 규모)
- 확장 타겟: 프리랜서 개발자, 오픈소스 프로젝트 관리자

## 핵심 기능

1. **자동 코드 분석**
   - 설명: PR이 생성되면 자동으로 코드를 분석하고 리뷰 코멘트 생성
   - 가치: 수동 리뷰 전 기본적인 이슈를 미리 해결

2. **보안 취약점 탐지**
   - 설명: OWASP Top 10 기반 보안 문제 자동 탐지
   - 가치: 보안 사고를 사전에 예방

3. **팀 컨벤션 학습**
   - 설명: 기존 코드베이스를 학습하여 팀 스타일 가이드 자동 적용
   - 가치: 일관된 코드 품질 유지

4. **실시간 피드백**
   - 설명: PR 생성 후 30초 이내 AI 리뷰 제공
   - 가치: 빠른 피드백 사이클

## 기술 스택
- Backend: Directus + Python (AI 로직용)
- AI/ML: OpenAI API, LangChain
- Queue: Redis + Celery (비동기 분석)

## 특별 요구사항
- [x] 실시간 알림 (WebSocket)
- [x] GitHub 통합 (Webhook)
- [x] AI/ML 기능 통합
- [x] 소셜 로그인 (GitHub OAuth)

## 예상 사용 시나리오

### 시나리오 1: PR 자동 리뷰
1. 개발자가 GitHub에 PR 생성
2. Webhook이 시스템에 PR 정보 전송
3. 시스템이 자동으로 코드 분석 시작 (30초 이내)
4. AI가 코드 품질, 보안, 컨벤션 검사
5. AI 리뷰 코멘트가 PR에 자동으로 등록됨
6. 개발자가 이슈를 수정하고 재분석 요청
7. 통과 시 팀원에게 리뷰 요청 알림

## 비즈니스 모델
- 무료: 오픈소스 프로젝트 무제한
- 프리미엄: 월 $29 (팀당, 5명까지)
- 엔터프라이즈: 커스텀 견적

## MVP 범위
- [x] GitHub PR 연동
- [x] 자동 코드 분석
- [x] 보안 취약점 탐지
- [ ] 팀 컨벤션 학습 (v2에서)
- [ ] 커스텀 룰셋 (v2에서)
```

### 1.2 스킬 실행

```bash
cd codereview-ai
# IDEA.md 작성 후
/idea-to-app
```

### 1.3 생성되는 구조

```
codereview-ai/
├── IDEA.md
├── README.md
├── docker-compose.yml
├── .env.example
├── .docker/
│   ├── mysql/
│   ├── directus/
│   └── redis/
├── docs/
│   ├── 01-PRD.md               # AI 리뷰 시스템 상세 요구사항
│   ├── 02-ARCHITECTURE.md      # Directus + Python AI Backend 구조
│   ├── 03-API_SPEC.md          # GitHub Webhook, 분석 API 등
│   ├── 04-DATABASE_SCHEMA.md   # projects, reviews, findings 등
│   ├── 05-DEVELOPMENT_GUIDE.md
│   ├── 06-DEPLOYMENT.md
│   └── 07-MVP_CHECKLIST.md
├── backend/                    # Python AI Backend
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── project.py
│   │   │   ├── review.py
│   │   │   └── finding.py
│   │   ├── routes/
│   │   │   ├── webhook.py
│   │   │   └── analysis.py
│   │   └── services/
│   │       ├── github.py
│   │       ├── ai_analyzer.py
│   │       └── security_checker.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Projects.tsx
│   │   │   └── Reviews.tsx
│   │   └── components/
│   │       ├── ReviewCard.tsx
│   │       └── FindingList.tsx
└── mobile/
    └── app/
        ├── (tabs)/
        │   ├── dashboard.tsx
        │   └── reviews.tsx
        └── review/[id].tsx
```

### 1.4 docker-compose.yml 예시

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: codereview
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    volumes:
      - ./.docker/mysql:/var/lib/mysql
    ports:
      - "3306:3306"

  redis:
    image: redis:7-alpine
    volumes:
      - ./.docker/redis:/data
    ports:
      - "6379:6379"

  directus:
    image: directus/directus:latest
    environment:
      KEY: your-secret-key
      SECRET: your-secret
      DB_CLIENT: mysql
      DB_HOST: mysql
      DB_PORT: 3306
      DB_DATABASE: codereview
      DB_USER: user
      DB_PASSWORD: password
      ADMIN_EMAIL: admin@example.com
      ADMIN_PASSWORD: admin
      CACHE_ENABLED: true
      CACHE_STORE: redis
      CACHE_REDIS: redis://redis:6379
    volumes:
      - ./.docker/directus/uploads:/directus/uploads
    ports:
      - "8055:8055"
    depends_on:
      - mysql
      - redis

  backend:
    build: ./backend
    environment:
      DATABASE_URL: mysql://user:password@mysql:3306/codereview
      REDIS_URL: redis://redis:6379
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      GITHUB_WEBHOOK_SECRET: ${GITHUB_WEBHOOK_SECRET}
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - mysql
      - redis
    command: uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

  celery-worker:
    build: ./backend
    environment:
      DATABASE_URL: mysql://user:password@mysql:3306/codereview
      REDIS_URL: redis://redis:6379
      OPENAI_API_KEY: ${OPENAI_API_KEY}
    volumes:
      - ./backend:/app
    depends_on:
      - mysql
      - redis
    command: celery -A src.celery_app worker --loglevel=info
```

---

## 예시 2: 간단한 블로그 플랫폼

### 2.1 IDEA.md

```markdown
# DevBlog

## 한 줄 소개
개발자를 위한 마크다운 기반 블로그 플랫폼

## 핵심 가치
- 마크다운으로 빠르게 작성
- 코드 하이라이팅 자동 지원
- SEO 최적화

## 타겟 사용자
- 주 타겟: 기술 블로거, 개발자

## 핵심 기능

1. **마크다운 포스트 작성**
   - 설명: 마크다운 에디터로 포스트 작성
   - 가치: 익숙한 문법으로 빠른 작성

2. **카테고리 및 태그**
   - 설명: 포스트를 카테고리와 태그로 분류
   - 가치: 체계적인 콘텐츠 관리

3. **댓글 시스템**
   - 설명: 포스트별 댓글 기능
   - 가치: 독자와 소통

4. **검색 기능**
   - 설명: 제목, 내용, 태그 기반 검색
   - 가치: 원하는 글 빠르게 찾기

## MVP 범위
- [x] 포스트 CRUD
- [x] 카테고리/태그
- [x] 검색
- [ ] 댓글 (v2)
```

### 2.2 스킬 실행

```bash
cd devblog
/idea-to-app
```

### 2.3 생성되는 구조 (Directus 기본 사용)

```
devblog/
├── IDEA.md
├── README.md
├── docker-compose.yml           # MySQL + Directus만
├── .env.example
├── docs/
│   ├── 01-PRD.md
│   ├── 02-ARCHITECTURE.md       # Directus 기본 아키텍처
│   ├── 03-API_SPEC.md           # Directus Collections API
│   ├── 04-DATABASE_SCHEMA.md    # posts, categories, tags Collections
│   ├── 05-DEVELOPMENT_GUIDE.md
│   ├── 06-DEPLOYMENT.md
│   └── 07-MVP_CHECKLIST.md
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Post.tsx
│   │   │   └── Editor.tsx
│   │   └── components/
│   │       ├── PostList.tsx
│   │       ├── MarkdownEditor.tsx
│   │       └── CategoryFilter.tsx
└── mobile/
    └── app/
        └── (tabs)/
            └── posts.tsx
```

**참고**: 커스텀 백엔드 없이 Directus만 사용하므로 `backend/` 디렉토리가 생성되지 않음

### 2.4 Directus Collections (04-DATABASE_SCHEMA.md에서)

```markdown
## Directus Collections

### posts
- id: UUID
- title: String(255)
- slug: String(255) - Unique
- content: Text (Markdown)
- excerpt: Text
- featured_image: File (Directus)
- status: String (draft, published)
- category_id: UUID → categories
- created_at: Timestamp
- updated_at: Timestamp
- user_created: UUID → directus_users

### categories
- id: UUID
- name: String(100)
- slug: String(100)
- description: Text

### tags
- id: UUID
- name: String(50)

### posts_tags (M2M)
- posts_id: UUID → posts
- tags_id: UUID → tags
```

---

## 예시 3: AI 이미지 생성 서비스

### 3.1 IDEA.md

```markdown
# ArtFlow AI

## 한 줄 소개
AI 기반 이미지 생성 및 편집 플랫폼

## 핵심 가치
- 텍스트만으로 고품질 이미지 생성
- 초보자도 쉽게 사용 가능한 UI
- 생성 기록 관리 및 재사용

## 타겟 사용자
- 주 타겟: 디자이너, 마케터, 콘텐츠 크리에이터
- 확장 타겟: 일반 사용자

## 핵심 기능

1. **텍스트-이미지 생성**
   - 설명: 프롬프트 입력으로 이미지 생성
   - 가치: 디자인 스킬 없이 이미지 제작

2. **스타일 프리셋**
   - 설명: 사전 정의된 스타일 (애니메이션, 사실적 등)
   - 가치: 빠른 스타일 적용

3. **생성 히스토리**
   - 설명: 과거 생성 기록 저장 및 재생성
   - 가치: 프롬프트 재사용 및 개선

4. **크레딧 시스템**
   - 설명: 사용량 기반 크레딧 차감
   - 가치: 명확한 비용 관리

## 기술 스택
- Backend: Python (FastAPI) - AI 통합 필수
- AI: Stable Diffusion API / DALL-E
- Storage: S3 (생성된 이미지 저장)

## 특별 요구사항
- [x] AI/ML 기능 통합
- [x] 대용량 파일 처리 (S3 연동)
- [x] 비동기 작업 (긴 생성 시간)
- [x] 결제 연동 (크레딧 구매)

## 비즈니스 모델
- 무료: 월 50 크레딧
- 프리미엄: 월 $19 (500 크레딧)
- 프로: 월 $49 (무제한)
```

### 3.2 생성되는 구조 (Python Backend 필수)

```
artflow-ai/
├── backend/
│   ├── src/
│   │   ├── services/
│   │   │   ├── stable_diffusion.py
│   │   │   ├── s3_storage.py
│   │   │   └── credit_manager.py
│   │   ├── routes/
│   │   │   ├── generation.py
│   │   │   └── credits.py
│   │   └── models/
│   │       ├── generation.py
│   │       └── credit_transaction.py
│   └── celery_app.py            # 비동기 작업
├── frontend/
│   └── src/
│       └── pages/
│           ├── Generator.tsx
│           ├── History.tsx
│           └── Gallery.tsx
└── mobile/
    └── app/
        └── generate.tsx
```

### 3.3 docker-compose.yml 추가 서비스

```yaml
  celery-worker:
    build: ./backend
    environment:
      CELERY_BROKER_URL: redis://redis:6379
      STABLE_DIFFUSION_API_KEY: ${SD_API_KEY}
      AWS_S3_BUCKET: ${S3_BUCKET}
    command: celery -A src.celery_app worker

  celery-beat:
    build: ./backend
    command: celery -A src.celery_app beat
```

---

## 스킬 실행 대화 예시

### 시작

```
사용자: /idea-to-app

Claude: IDEA.md 파일을 분석했습니다.

📋 프로젝트 정보:
- 프로젝트명: CodeReview AI
- 핵심 기능: 4개
- 기술 스택: Directus + Python (AI 로직)
- 특별 요구사항: AI/ML, GitHub 연동, 실시간 알림

이 내용으로 진행할까요? (Y/n)
```

### 문서 생성

```
사용자: Y

Claude: 문서를 생성하겠습니다.

✅ docs/01-PRD.md 생성 완료
   - 4개 핵심 기능 상세 정의
   - 사용자 페르소나 2개 추가
   - MVP 범위 정의

계속 진행할까요? (Y/n)

사용자: Y

Claude: ✅ docs/02-ARCHITECTURE.md 생성 완료
   - Directus + Python 하이브리드 아키텍처
   - AI 분석 비동기 처리 (Celery)
   - GitHub Webhook 통합 구조

✅ docs/03-API_SPEC.md 생성 완료
✅ docs/04-DATABASE_SCHEMA.md 생성 완료
✅ docs/05-DEVELOPMENT_GUIDE.md 생성 완료
✅ docs/06-DEPLOYMENT.md 생성 완료
✅ docs/07-MVP_CHECKLIST.md 생성 완료

프로젝트 구조를 생성할까요? (Y/n)
```

### 구조 생성

```
사용자: Y

Claude: 프로젝트 구조를 생성합니다...

✅ docker-compose.yml (MySQL, Directus, Redis, Backend, Celery)
✅ .env.example
✅ backend/ (Python + FastAPI + AI 로직)
✅ frontend/ (React + TypeScript)
✅ mobile/ (Expo)

🎉 모든 설정이 완료되었습니다!

🚀 다음 단계:

1. 환경 변수 설정
   cp .env.example .env
   # .env에서 OPENAI_API_KEY, GITHUB_WEBHOOK_SECRET 설정

2. Docker 실행
   docker-compose up -d

3. Directus 초기 설정
   - http://localhost:8055 접속
   - 관리자 계정 생성
   - Collections 생성 (docs/04-DATABASE_SCHEMA.md 참고)

4. 개발 시작
   cd frontend && pnpm dev

구현을 시작할까요? 어떤 부분부터 시작하시겠어요?
[1] Directus Collection 설정
[2] Backend AI 서비스 구현
[3] Frontend 기본 UI
[4] 전체 MVP 단계별 진행
```

---

## 핵심 포인트

1. **IDEA.md만 잘 작성하면 끝**
   - 핵심 기능을 명확히
   - 기술 스택 특별 요구사항이 있으면 명시

2. **단계별 확인**
   - 문서 생성 후 검토
   - 구조 생성 전 확인

3. **자동 판단**
   - AI 기능 → Python Backend 자동 추가
   - 기본 CRUD만 → Directus만 사용
   - 실시간 → Redis 자동 추가

4. **즉시 개발 가능**
   - docker-compose up 하나로 환경 준비
   - 문서를 따라가면 구현 가능

---

**예시 버전**: 1.0.0
**업데이트**: 2026-01-28

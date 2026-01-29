# 문서 템플릿

## CLAUDE.md 템플릿

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**{프로젝트명}**은(는) {한 줄 설명} 플랫폼입니다. 서비스명은 {서비스명}입니다.

핵심 기능:
- {기능1}
- {기능2}
- {기능3}

## Target Architecture (Monorepo)

\`\`\`
apps/web/              # {웹 프레임워크} 웹 앱
apps/mobile/           # {모바일 프레임워크} 앱
services/api/          # {백엔드 프레임워크} API
services/worker/       # 백그라운드 워커
infra/                 # 인프라 설정
packages/shared/       # 공유 타입/스키마
docs/                  # 문서
\`\`\`

## Tech Stack

- **Frontend**: {프론트엔드 스택}
- **Backend**: {백엔드 스택}
- **Auth/Storage**: {인증/저장소}
- **Workflows**: {워크플로우 도구}

## Key Design Considerations

- {설계 고려사항 1}
- {설계 고려사항 2}
- {설계 고려사항 3}
```

---

## docs/01-prd.md 템플릿

```markdown
# 제품 요구사항 정의서 (PRD)

## 1. 제품 개요

| 항목 | 내용 |
|------|------|
| 프로젝트명 | {프로젝트명} |
| 서비스명 | {서비스명} |
| 한 줄 정의 | {한 줄 설명} |
| USP | {고유 가치 제안} |

---

## 2. 타겟 사용자

### 2.1 1차 타겟

| 구분 | 내용 |
|------|------|
| 대상 | {1차 타겟} |
| 니즈 | {니즈} |

### 2.2 확장 타겟

| 구분 | 내용 |
|------|------|
| 대상 | {확장 타겟} |
| 니즈 | {니즈} |

---

## 3. 솔루션

{솔루션 설명}

---

## 4. 사용자 핵심 플로우

\`\`\`
[단계1] → [단계2] → [단계3] → [단계4]
\`\`\`

### 상세 플로우

1. **{단계1}**: {설명}
2. **{단계2}**: {설명}
3. **{단계3}**: {설명}

---

## 5. 기능 요구사항

### 5.1 {카테고리1}

| 기능 | 설명 | 우선순위 |
|------|------|----------|
| {기능1} | {설명} | P0 |
| {기능2} | {설명} | P1 |

### 5.2 {카테고리2}

| 기능 | 설명 | 우선순위 |
|------|------|----------|
| {기능1} | {설명} | P0 |

---

## 6. 비기능 요구사항

| 영역 | 요구사항 |
|------|----------|
| 성능 | {요구사항} |
| 보안 | {요구사항} |
| 확장성 | {요구사항} |

---

## 7. MVP 범위

### 포함

- {포함 항목1}
- {포함 항목2}

### 제외

- {제외 항목1}
- {제외 항목2}

---

## 8. KPI

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| {지표1} | {목표} | {방법} |
| {지표2} | {목표} | {방법} |

---

## 9. 수익 모델

| 모델 | 설명 |
|------|------|
| {모델} | {설명} |
```

---

## docs/02-architecture.md 템플릿

```markdown
# 시스템 아키텍처

## 1. 모노레포 구조

\`\`\`
{project}/
├── apps/
│   ├── web/                    # 웹 앱
│   └── mobile/                 # 모바일 앱
├── services/
│   ├── api/                    # API 서버
│   └── worker/                 # 워커
├── infra/
│   └── {인프라 구성}/
├── packages/
│   └── shared/                 # 공유 패키지
└── docs/
\`\`\`

---

## 2. 기술 스택

| 영역 | 기술 | 비고 |
|------|------|------|
| Web | {웹 스택} | {비고} |
| Mobile | {모바일 스택} | {비고} |
| Backend | {백엔드 스택} | {비고} |
| Database | {DB} | {비고} |
| Auth | {인증} | {비고} |

---

## 3. 데이터 흐름

\`\`\`
[클라이언트] → [API] → [서비스] → [DB]
                 ↓
            [워커/큐]
\`\`\`

---

## 4. 데이터 모델

### {모델1}

\`\`\`python
class {Model1}(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # 필드들
\`\`\`

---

## 5. 핵심 설계 포인트

- {포인트1}
- {포인트2}
- {포인트3}
```

---

## docs/04-api-spec.md 템플릿

```markdown
# API 명세

## 1. 개요

| 항목 | 값 |
|------|-----|
| Base URL | \`/api/v1\` |
| 인증 | Bearer Token |
| 형식 | JSON |

---

## 2. 엔드포인트 목록

### {카테고리}

| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | \`/{resource}\` | 생성 |
| GET | \`/{resource}\` | 목록 조회 |
| GET | \`/{resource}/{id}\` | 상세 조회 |
| PUT | \`/{resource}/{id}\` | 수정 |
| DELETE | \`/{resource}/{id}\` | 삭제 |

---

## 3. 스키마

### Request

\`\`\`python
class {Resource}CreateRequest(BaseModel):
    field1: str
    field2: int
\`\`\`

### Response

\`\`\`python
class {Resource}Response(BaseModel):
    id: int
    field1: str
    created_at: datetime
\`\`\`

---

## 4. 에러 코드

| 코드 | HTTP | 설명 |
|------|------|------|
| {ERROR_CODE} | 400 | {설명} |
```

---

## docs/06-dev-guide.md 템플릿

```markdown
# 개발 가이드

## 1. 개발 환경

### 1.1 필수 도구

| 도구 | 버전 | 용도 |
|------|------|------|
| Node.js | 20+ | Frontend |
| Python | 3.11+ | Backend |
| {도구} | {버전} | {용도} |

### 1.2 초기 설정

\`\`\`bash
# 저장소 클론
git clone {repo-url}
cd {project}

# 의존성 설치
{패키지 매니저} install

# 개발 서버 실행
{실행 명령}
\`\`\`

---

## 2. 코딩 컨벤션

### Python

\`\`\`python
# 파일명: snake_case
# 클래스: PascalCase
# 함수/변수: snake_case
\`\`\`

### TypeScript

\`\`\`typescript
// 파일명: kebab-case.tsx
// 컴포넌트: PascalCase
// 함수/변수: camelCase
\`\`\`

---

## 3. Git 컨벤션

\`\`\`bash
# 브랜치
feature/{기능명}
fix/{버그명}

# 커밋
feat: {설명}
fix: {설명}
docs: {설명}
\`\`\`
```

---

## docs/07-mvp-checklist.md 템플릿

```markdown
# MVP 구현 체크리스트

## 개요

| 항목 | 내용 |
|------|------|
| 목표 | {MVP 목표} |
| 예상 Phase | {N}개 |

---

## Phase 1: 프로젝트 초기화

- [ ] 모노레포 구조 생성
- [ ] 패키지 의존성 설정
- [ ] 개발 환경 설정

## Phase 2: 인증 시스템

- [ ] 사용자 모델 정의
- [ ] 로그인/회원가입 API
- [ ] 인증 미들웨어

## Phase 3: {핵심 기능1}

- [ ] {항목1}
- [ ] {항목2}
- [ ] {항목3}

## Phase N: 통합 및 마무리

- [ ] 전체 플로우 테스트
- [ ] 에러 처리 검증
- [ ] 배포 준비

---

## 구현 우선순위

| 순서 | 기능 | 상태 |
|------|------|------|
| 1 | 프로젝트 초기화 | 대기 |
| 2 | 인증 시스템 | 대기 |
| 3 | {핵심 기능} | 대기 |
```

---

## .cursorrules 템플릿

```markdown
# {프로젝트명} - AI Coding Rules

## 프로젝트 개요

- 프로젝트명: {프로젝트명}
- 서비스명: {서비스명}
- 목적: {한 줄 설명}

## 문서 참조

코드 작성 전 반드시 참조:
- docs/01-prd.md: 제품 요구사항
- docs/02-architecture.md: 시스템 아키텍처
- docs/04-api-spec.md: API 명세
- docs/06-dev-guide.md: 개발 가이드

## 기술 스택

### Backend
- {백엔드 스택}

### Frontend
- {프론트엔드 스택}

## 코딩 컨벤션

### Python

\`\`\`python
# 타입 힌트 필수
async def get_item(item_id: int) -> Item:
    pass
\`\`\`

### TypeScript

\`\`\`typescript
// interface 우선 사용
interface Item {
  id: number;
  name: string;
}
\`\`\`

## Git 컨벤션

\`\`\`bash
feat: 기능 추가
fix: 버그 수정
docs: 문서 수정
\`\`\`
```

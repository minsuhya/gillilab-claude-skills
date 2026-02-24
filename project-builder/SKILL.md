---
name: project-builder
description: >
  서비스 컨셉 또는 IDEA.md로부터 프로젝트 문서(PRD, 아키텍처, API 명세, 개발 가이드)와
  프로젝트 구조(Backend/Frontend/Mobile)를 체계적으로 생성하고, 서브 에이전트를 조율하여
  풀스택 웹 애플리케이션을 구현한다.
  "풀스택", "웹앱 만들어", "앱 개발", "fullstack", "full-stack", "web app",
  "아이디어를 앱으로", "IDEA.md로 앱", "프로젝트 빌더", "idea to app",
  "project builder", "앱 만들어줘", "서비스 문서 만들어줘", "프로젝트 문서 생성",
  "service docs generator" 등의 키워드로 트리거.
---

# Project Builder

서비스 컨셉 또는 IDEA.md 하나로 문서 생성 → 프로젝트 구조 생성 → 풀스택 구현까지 수행한다.

## 진입 모드 판별

| 조건 | 모드 | 시작 Phase |
|------|------|-----------|
| IDEA.md 존재 | Idea-to-App | Phase 1 |
| 서비스 컨셉만 제공 | Docs-First | Phase 0 |
| 기존 docs/ + 코드 요청 | Build-Only | Phase 3 |

Build-Only 모드에서 docs/가 불완전한 경우, 누락된 문서를 Phase 1에서 먼저 보완한 후 Phase 3을 진행한다.

IDEA.md가 없으면 [assets/IDEA_TEMPLATE.md](assets/IDEA_TEMPLATE.md) 템플릿을 제공하여 작성을 안내한다.

## Phase 0: 컨셉 수집 (Docs-First 모드)

AskUserQuestion으로 수집:

**필수**: 프로젝트명, 서비스명, 한 줄 설명, 타겟 사용자, 핵심 기능 3-5개, 기술 스택
**선택**: 비즈니스 모델, MVP 범위, 특수 요구사항 (AI, 실시간, 오프라인)

## Phase 1: 문서 생성

각 문서 생성 후 사용자 확인을 구한다.

```
{project}/
├── README.md
├── CLAUDE.md                    # AI 코딩 가이드 (선택)
└── docs/
    ├── 01-prd.md               # 제품 요구사항 정의서
    ├── 02-architecture.md      # 시스템 아키텍처
    ├── 03-{domain}-strategy.md # 도메인별 전략
    ├── 04-api-spec.md          # API 명세
    ├── 05-roadmap.md           # 개발 로드맵
    ├── 06-dev-guide.md         # 개발 가이드
    ├── 07-mvp-checklist.md     # MVP 구현 체크리스트
    └── policies/               # 정책 문서
```

| 문서 | 필수 섹션 |
|------|-----------|
| **01-prd.md** | 제품 개요, 타겟, 솔루션, 핵심 플로우, 기능/비기능 요구사항, MVP 범위, KPI |
| **02-architecture.md** | 모노레포 구조, 기술 스택, 데이터 흐름(ASCII), ERD, 확장 전략 |
| **03-{domain}-strategy.md** | 서비스 특성에 따라: AI / 콘텐츠 / 커머스 전략 등 |
| **04-api-spec.md** | Base URL, 인증, 엔드포인트, 요청/응답 스키마, 에러 모델 |
| **05-roadmap.md** | 릴리즈 단계 (R0 MVP, R1, R2...), 핵심 원칙, 리스크 완화 |
| **06-dev-guide.md** | 개발 환경, 코딩 컨벤션, API/Frontend 패턴, 테스트, 배포 |
| **07-mvp-checklist.md** | Phase별 체크박스, 구현 우선순위 테이블 |

문서 템플릿: [references/doc-templates.md](references/doc-templates.md)
사용 예시: [references/doc-examples.md](references/doc-examples.md)

## Phase 2: 프로젝트 구조 생성

사용자 확인 후 디렉터리와 보일러플레이트를 생성한다.

### Backend 선택 기준

| 조건 | 선택 |
|------|------|
| 기본 CRUD만 필요 | Directus만 (외부 MySQL 연동) |
| 복잡한 비즈니스 로직 | Directus + Python (FastAPI + SQLModel) |
| IDEA.md에 명시된 스택 | 해당 스택 사용 |

### 기본 기술 스택

| 영역 | 기술 |
|------|------|
| Database | MySQL 8.0 (외부 통합 권장) |
| CMS/API | Directus (Docker) |
| Custom Backend | Python 3.11 + FastAPI + SQLModel (선택) |
| Frontend | React 19 + TypeScript + Vite + Tailwind CSS v4 |
| State | React Query + Zustand |
| Mobile | Expo SDK + React Native + NativeWind (선택) |
| DevOps | Docker + Docker Compose |

IDEA.md에 다른 기술 스택이 명시되어 있으면 해당 스택을 따른다.

구조 템플릿: [references/project-templates.md](references/project-templates.md)

## Phase 3: 풀스택 구현

서브 에이전트를 조율하여 순차/병렬로 구현한다.

### 실행 순서

| 순서 | 담당 | 입력 | 산출물 | 실행 |
|------|------|------|--------|------|
| 1 | database | 데이터 모델 요구사항 | schema.sql, models | 순차 |
| 2+3 | backend + frontend | models + API 명세 | API 서버 + 프론트엔드 앱 | **병렬** |
| 4 | testing | 전체 코드베이스 | 테스트 코드, 체크리스트 | 순차 |

backend와 frontend는 API 명세(04-api-spec.md)를 공유 인터페이스로 병렬 실행 가능하다.

오케스트레이션 상세: [references/orchestration_guide.md](references/orchestration_guide.md)

### 서브 에이전트 실행

각 단계의 산출물을 다음 단계의 입력으로 전달한다. 각 단계 완료 후:
1. 호환성 검증
2. 누락 사항 확인
3. 필요 시 재작업 지시

## Phase 4: 테스트 및 검증

- Docker 서비스 정상 실행 확인
- API 엔드포인트 테스트
- Frontend/Mobile 로컬 실행 확인
- 문서와 구현 일치 여부 확인

Docker 미설치 환경에서는 Phase 1-2만 수행하고 환경 준비 후 안내한다.

## 문서 작성 규칙

- 모든 문서는 한국어로 작성
- 파일명: 숫자 접두사 + 소문자 + 하이픈 (예: `01-prd.md`)
- 문서 간 중복 없이 상호 참조 사용
- 코드 예시는 기술 스택에 맞게 작성
- 체크리스트는 실행 가능한 수준으로 구체적 작성

## 리소스

- [assets/IDEA_TEMPLATE.md](assets/IDEA_TEMPLATE.md): IDEA.md 작성 템플릿
- [references/doc-templates.md](references/doc-templates.md): 문서 템플릿 (서비스 문서 + IDEA 기반 문서)
- [references/doc-examples.md](references/doc-examples.md): 문서 사용 예시 (서비스 문서 + IDEA 기반 예시)
- [references/project-templates.md](references/project-templates.md): 프로젝트 구조 템플릿
- [references/orchestration_guide.md](references/orchestration_guide.md): 서브 에이전트 조율 가이드, 데모 예시, 에이전트 시스템 가이드 포함

## 주의사항

- 이미 존재하는 파일은 덮어쓰지 않는다 (사용자 확인 후 진행)
- 각 Phase 완료 후 사용자 확인을 거친다
- 서비스 특성에 맞게 도메인 전략 문서명을 변경한다

# idea-to-app 문서 템플릿

이 파일은 스킬이 생성하는 각 문서의 템플릿을 정의합니다.

---

## 1. PRD (제품 요구사항 정의서)

**파일명**: `docs/01-PRD.md`

```markdown
# [프로젝트명] - 제품 요구사항 정의서 (PRD)

> 버전: 1.0 | 작성일: [날짜] | 작성자: [이름]

## 1. 제품 개요

### 1.1 프로젝트 정보

- **프로젝트명**: [내부 코드명]
- **서비스명**: [사용자에게 보이는 이름]
- **한 줄 정의**: [IDEA.md에서 추출]

### 1.2 핵심 가치 제안 (USP)

[IDEA.md의 핵심 가치를 확장하여 작성]

1. [가치 1]
2. [가치 2]
3. [가치 3]

## 2. 타겟 사용자

### 2.1 주 타겟 사용자

[IDEA.md에서 추출하여 상세화]

**특징**:

- 인구통계: [연령, 직업 등]
- 행동 패턴: [사용 패턴]
- 니즈: [주요 니즈]
- 페인 포인트: [현재 겪는 문제]

### 2.2 확장 타겟 사용자

[IDEA.md에서 추출하여 상세화]

### 2.3 사용자 페르소나

**페르소나 1: [이름]**

- 배경: [설명]
- 목표: [목표]
- 문제: [겪는 문제]
- 기대: [이 서비스에 기대하는 것]

## 3. 핵심 사용자 플로우

### 플로우 1: [주요 플로우 이름]

1. [단계 1]
2. [단계 2]
3. [단계 3]

[IDEA.md의 시나리오를 기반으로 주요 플로우 작성]

## 4. 기능 요구사항

### 4.1 핵심 기능 (MVP)

#### [기능 1 이름]

- **설명**: [IDEA.md에서 추출]
- **사용자 스토리**:
  - As a [사용자], I want to [행동], so that [목적]
- **Acceptance Criteria**:
  - [ ] [조건 1]
  - [ ] [조건 2]
- **우선순위**: P0 (Critical)

[IDEA.md의 모든 핵심 기능을 이렇게 확장]

### 4.2 부가 기능 (Post-MVP)

[향후 추가될 기능들]

## 5. 비기능 요구사항

### 5.1 성능

- 페이지 로드 시간: < 2초
- API 응답 시간: < 500ms (p95)
- 동시 접속자: [예상 수치]

### 5.2 보안

- 사용자 인증: JWT 기반
- 데이터 암호화: TLS 1.3
- OWASP Top 10 대응

### 5.3 확장성

- 수평 확장 가능한 아키텍처
- 데이터베이스 레플리케이션
- CDN 활용

### 5.4 사용성

- 모바일 반응형 디자인
- 접근성 (WCAG 2.1 AA 준수)
- 다국어 지원 (필요시)

## 6. 기술 제약사항

### 6.1 기술 스택

[IDEA.md에서 지정된 스택 또는 기본 스택]

- Database: MySQL
- Backend: Directus / Python
- Frontend: React + TypeScript
- Mobile: Expo

### 6.2 통합

- [필요한 외부 API 통합]
- [결제 시스템 등]

## 7. MVP 범위

### 포함 (In)

- [x] [기능 1]
- [x] [기능 2]

### 제외 (Out)

- [ ] [기능 N] - Post-MVP

## 8. 성공 지표 (KPI)

### 비즈니스 지표

- 사용자 수: [목표]
- DAU/MAU: [목표]
- 전환율: [목표]

### 기술 지표

- 가동률: 99.9%
- 평균 응답 시간: < 500ms
- 에러율: < 0.1%

## 9. 프로젝트 일정

- Phase 1 (MVP): [기간]
- Phase 2 (확장): [기간]

## 10. 위험 요소 및 완화 전략

| 위험     | 영향 | 완화 전략 |
| -------- | ---- | --------- |
| [위험 1] | High | [전략]    |

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]
```

---

## 2. ARCHITECTURE (시스템 아키텍처)

**파일명**: `docs/02-ARCHITECTURE.md`

````markdown
# [프로젝트명] - 시스템 아키텍처

> 버전: 1.0 | 작성일: [날짜]

## 1. 개요

이 문서는 [프로젝트명]의 전체 시스템 아키텍처를 정의합니다.

## 2. 프로젝트 구조

```bash
project-root/
├── IDEA.md
├── README.md
├── docker-compose.yml          # Docker 서비스 정의
├── .env.example
├── .docker/                    # Docker 마운트 디렉토리
│   ├── mysql/
│   ├── directus/
│   └── redis/
├── docs/                       # 프로젝트 문서
│   ├── 01-PRD.md
│   ├── 02-ARCHITECTURE.md
│   ├── 03-API_SPEC.md
│   ├── 04-DATABASE_SCHEMA.md
│   ├── 05-DEVELOPMENT_GUIDE.md
│   ├── 06-DEPLOYMENT.md
│   └── 07-MVP_CHECKLIST.md
├── backend/                    # Custom Backend (선택)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       ├── main.py
│       ├── models/
│       ├── routes/
│       └── services/
├── frontend/                   # React Frontend
│   ├── package.json
│   └── src/
│       ├── pages/
│       ├── components/
│       └── lib/
└── mobile/                     # Expo Mobile
    ├── package.json
    ├── app/
    └── components/
```
````

## 3. 기술 스택

### 3.1 Backend

| 구성 요소      | 기술             | 버전   | 용도                 |
| -------------- | ---------------- | ------ | -------------------- |
| Database       | MySQL            | 8.0    | 메인 데이터베이스    |
| CMS/API        | Directus         | 10+    | 기본 API 및 관리     |
| Custom Backend | Python + FastAPI | 3.11+  | 커스텀 로직 (필요시) |
| ORM            | SQLModel         | latest | 데이터 모델링        |
| Validation     | Pydantic         | v2     | 데이터 검증          |
| Cache          | Redis            | 7+     | 캐싱 및 세션         |

### 3.2 Frontend

| 구성 요소       | 기술                  | 버전   | 용도          |
| --------------- | --------------------- | ------ | ------------- |
| Framework       | React                 | 19+    | UI 프레임워크 |
| Language        | TypeScript            | 5.9+   | 타입 안정성   |
| Build Tool      | Vite                  | 7+     | 빌드 도구     |
| Styling         | Tailwind CSS          | 4+     | 스타일링      |
| State           | React Query + Zustand | 5+     | 상태 관리     |
| Form            | React Hook Form + Zod | 7+/4+  | 폼 관리/검증  |
| Package Manager | pnpm                  | 9+     | 의존성 관리   |

### 3.3 Mobile

| 구성 요소  | 기술        | 버전    | 용도                           |
| ---------- | ----------- | ------- | ------------------------------ |
| Framework  | Expo        | SDK 54+ | React Native 개발              |
| Runtime    | React Native| 0.81+   | 모바일 앱 런타임               |
| Language   | TypeScript  | 5+      | 타입 안정성                    |
| Navigation | Expo Router | 6+      | 파일 기반 라우팅               |
| UI         | NativeWind  | v4      | Tailwind for RN (Tailwind v3 기반) |

### 3.4 DevOps

| 구성 요소  | 기술                    | 용도                   |
| ---------- | ----------------------- | ---------------------- |
| Container  | Docker + Docker Compose | 로컬 개발 및 운영 환경 |
| CI/CD      | GitHub Actions          | 자동화된 배포          |
| Monitoring | (선택)                  | 모니터링               |

## 4. 시스템 다이어그램

### 4.1 전체 아키텍처

```
┌─────────────┐     ┌─────────────┐
│   Browser   │     │   Mobile    │
│  (Frontend) │     │    (Expo)   │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └───────┬───────────┘
               │ HTTPS
               ▼
       ┌───────────────┐
       │  API Gateway  │
       │   (Nginx)     │
       └───────┬───────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
┌─────────────┐  ┌──────────────┐
│  Directus   │  │   Custom     │
│  (Default)  │  │   Backend    │
│             │  │  (Optional)  │
└──────┬──────┘  └──────┬───────┘
       │                │
       └────────┬───────┘
                │
        ┌───────┴───────┐
        │               │
        ▼               ▼
   ┌─────────┐     ┌────────┐
   │  MySQL  │     │ Redis  │
   └─────────┘     └────────┘
```

### 4.2 데이터 흐름

```
User Request
    │
    ├─ Authentication (JWT)
    │
    ├─ API Request
    │   │
    │   ├─ Directus API (기본 CRUD)
    │   │   └─ MySQL
    │   │
    │   └─ Custom API (복잡한 로직)
    │       ├─ Business Logic
    │       ├─ MySQL (SQLModel)
    │       └─ Redis (Cache)
    │
    └─ Response (JSON)
```

## 5. 데이터 모델

[docs/04-DATABASE_SCHEMA.md에서 상세 정의]

주요 엔티티:

- [엔티티 1]
- [엔티티 2]
- [엔티티 3]

## 6. API 설계

[docs/03-API_SPEC.md에서 상세 정의]

### 6.1 Directus 기본 API

- `/items/[collection]` - CRUD 작업
- `/users` - 사용자 관리
- `/auth` - 인증

### 6.2 Custom API (필요시)

- `/api/v1/[custom-endpoint]` - 커스텀 로직

## 7. 보안 설계

### 7.1 인증 및 권한

- JWT 기반 인증
- Role-Based Access Control (RBAC)
- Directus의 권한 시스템 활용

### 7.2 데이터 보호

- 전송 중 암호화: TLS 1.3
- 저장 암호화: 민감 필드 암호화
- 비밀번호 해싱: bcrypt

### 7.3 API 보안

- Rate Limiting
- CORS 설정
- Input Validation

## 8. 확장성 전략

### 8.1 수평 확장

- Stateless API 서버
- 로드 밸런서 사용
- 데이터베이스 읽기 복제본

### 8.2 성능 최적화

- Redis 캐싱
- CDN 활용 (정적 자산)
- 데이터베이스 인덱싱

## 9. 배포 아키텍처

### 9.1 로컬 개발

```bash
docker-compose up
# Frontend: pnpm dev (http://localhost:5173)
# Backend: http://localhost:8000
# Directus: http://localhost:8055
```

### 9.2 운영 환경

**Backend Services** (Docker 컨테이너):
- Directus
- Redis
- Custom Backend (필요 시)

**Frontend** (정적 파일 배포):
```bash
cd frontend
pnpm build
# dist/ 디렉토리를 Host Nginx/Apache 등으로 배포
```

**예시 Nginx 설정**:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /var/www/html/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## 10. 모니터링 및 로깅

### 10.1 모니터링

- 애플리케이션 메트릭
- 인프라 메트릭
- 에러 추적

### 10.2 로깅

- 구조화된 로그 (JSON)
- 중앙화된 로그 수집

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]

````

---

## 3. API_SPEC (API 명세서)

**파일명**: `docs/03-API_SPEC.md`

```markdown
# [프로젝트명] - API 명세서

> 버전: 1.0 | 작성일: [날짜]

## 1. 개요

### 1.1 Base URL
- 로컬: `http://localhost:8055` (Directus)
- 로컬: `http://localhost:8000` (Custom Backend)
- 운영: `https://api.[domain].com`

### 1.2 인증 방식
- Type: JWT Bearer Token
- Header: `Authorization: Bearer <token>`

### 1.3 공통 응답 형식

**성공 응답**:
```json
{
  "data": { ... }
}
````

**에러 응답**:

```json
{
  "errors": [
    {
      "message": "Error message",
      "extensions": {
        "code": "ERROR_CODE"
      }
    }
  ]
}
```

## 2. Directus 기본 API

### 2.1 인증

#### 로그인

```
POST /auth/login
```

**Request**:

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

**Response**:

```json
{
  "data": {
    "access_token": "eyJ...",
    "refresh_token": "abc...",
    "expires": 900000
  }
}
```

#### 토큰 갱신

```
POST /auth/refresh
```

### 2.2 컬렉션 CRUD

[PRD의 각 기능에 대해 Directus Collection API 정의]

#### [Collection 1] 조회

```
GET /items/[collection_name]
```

**Query Parameters**:

- `fields`: 조회할 필드 (예: `id,name,created_at`)
- `filter`: 필터 조건 (예: `{"status":{"_eq":"active"}}`)
- `sort`: 정렬 (예: `-created_at`)
- `limit`: 페이지 크기 (기본: 100)
- `page`: 페이지 번호

**Response**:

```json
{
  "data": [
    {
      "id": 1,
      "name": "...",
      "created_at": "2026-01-28T00:00:00Z"
    }
  ],
  "meta": {
    "total_count": 100,
    "filter_count": 10
  }
}
```

[각 주요 컬렉션에 대해 반복]

## 3. Custom API (필요시)

[복잡한 비즈니스 로직이 필요한 API 정의]

### 3.1 [Custom Endpoint 1]

```
POST /api/v1/[endpoint]
```

**Request**:

```json
{
  "param1": "value",
  "param2": 123
}
```

**Response**:

```json
{
  "result": "..."
}
```

**에러 코드**:

- `400`: Bad Request
- `401`: Unauthorized
- `404`: Not Found
- `500`: Internal Server Error

## 4. WebHook (내부용)

[필요시 WebHook 정의]

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]

````

---

## 4. DATABASE_SCHEMA (데이터베이스 스키마)

**파일명**: `docs/04-DATABASE_SCHEMA.md`

```markdown
# [프로젝트명] - 데이터베이스 스키마

> 버전: 1.0 | 작성일: [날짜]

## 1. 개요

- Database: MySQL 8.0
- ORM: SQLModel (Custom Backend) / Directus ORM
- Migration: Directus Migrations / Alembic

## 2. ERD (Entity Relationship Diagram)

````

[PRD의 기능을 기반으로 주요 엔티티 간 관계 다이어그램 텍스트로 표현]

┌────────────┐ ┌────────────┐
│ Users │───────│ Posts │
│ │ 1 N │ │
└────────────┘ └────────────┘
│ │
│ 1 N │
│ │
▼ ▼
┌────────────┐ ┌────────────┐
│ Profiles │ │ Comments │
└────────────┘ └────────────┘

````

## 3. Directus Collections

### 3.1 Users (Directus 기본)
Directus의 기본 사용자 컬렉션 사용

추가 필드:
- `custom_field_1`: [타입] - [설명]

### 3.2 [Collection 1 이름]

**컬렉션 정보**:
- Collection Name: `[collection_name]`
- Note: [용도 설명]

**필드 정의**:

| 필드명 | 타입 | 옵션 | 기본값 | 설명 |
|--------|------|------|--------|------|
| id | UUID | PK, Required | auto | 고유 식별자 |
| name | String(255) | Required | - | [설명] |
| status | String(20) | Required | 'draft' | draft, published, archived |
| created_at | Timestamp | Auto | NOW() | 생성 시각 |
| updated_at | Timestamp | Auto | NOW() | 수정 시각 |
| user_created | UUID | FK | - | 생성자 (users.id) |

**관계**:
- `user_created` → `directus_users.id` (Many-to-One)

**인덱스**:
- `idx_status`: (status)
- `idx_created_at`: (created_at DESC)

[PRD의 각 핵심 기능에 필요한 Collection 반복]

## 4. SQLModel 정의 (Custom Backend 사용 시)

### 4.1 [Model 1]

```python
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional

class [ModelName]Base(SQLModel):
    name: str = Field(max_length=255, index=True)
    status: str = Field(default="draft", max_length=20)

class [ModelName](ModelNameBase, table=True):
    __tablename__ = "[table_name]"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: UUID = Field(foreign_key="users.id")

    # Relationships
    user: Optional["User"] = Relationship(back_populates="[items]")

class [ModelName]Create(ModelNameBase):
    pass

class [ModelName]Read(ModelNameBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
````

[각 주요 모델 반복]

## 5. Migration 전략

### 5.1 Directus

```bash
# Schema Snapshot
npx directus schema snapshot ./snapshots/snapshot.yaml

# Schema Apply
npx directus schema apply ./snapshots/snapshot.yaml
```

### 5.2 Custom Backend (Alembic)

```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head
```

## 6. 데이터 정합성

### 6.1 제약 조건

- Foreign Key Constraints
- Unique Constraints
- Check Constraints

### 6.2 인덱스 전략

[성능 최적화를 위한 인덱스 정의]

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]

````

---

## 5. DEVELOPMENT_GUIDE (개발 가이드)

**파일명**: `docs/05-DEVELOPMENT_GUIDE.md`

```markdown
# [프로젝트명] - 개발 가이드

> 버전: 1.0 | 작성일: [날짜]

## 1. 개발 환경 설정

### 1.1 필수 도구

- Docker Desktop (최신 버전)
- Node.js 18+ & pnpm 8+
- Python 3.11+ (Custom Backend 사용 시)
- Git

### 1.2 초기 설정

```bash
# 1. 저장소 클론
git clone [repository-url]
cd [project-name]

# 2. 환경 변수 설정
cp .env.example .env
# .env 파일 편집

# 3. Docker 서비스 시작
docker-compose up -d

# 4. Directus 초기화 (최초 1회)
# http://localhost:8055 접속하여 관리자 계정 생성

# 5. Frontend 개발 서버
cd frontend
pnpm install
pnpm dev

# 6. Mobile 개발 서버
cd mobile
pnpm install
pnpm start
````

### 1.3 개발 서버 URL

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000 (Custom)
- Directus: http://localhost:8055
- MySQL: localhost:3306
- Redis: localhost:6379

## 2. 프로젝트 구조

[상세한 디렉토리 구조 및 파일 설명]

## 3. 코딩 컨벤션

### 3.1 Python (Backend)

- Style Guide: PEP 8
- Formatter: black
- Linter: ruff
- Type Checking: mypy

```python
# Good example
from typing import Optional
from sqlmodel import Field

async def get_user(user_id: str) -> Optional[User]:
    """사용자 조회

    Args:
        user_id: 사용자 ID

    Returns:
        User 객체 또는 None
    """
    return await db.get(User, user_id)
```

### 3.2 TypeScript (Frontend/Mobile)

- Style Guide: Airbnb + Custom
- Formatter: Prettier
- Linter: ESLint

```typescript
// Good example
interface UserProps {
  name: string;
  email: string;
}

export const UserCard: React.FC<UserProps> = ({ name, email }) => {
  return (
    <div className="user-card">
      <h3>{name}</h3>
      <p>{email}</p>
    </div>
  );
};
```

## 4. Git 워크플로우

### 4.1 브랜치 전략

- `main`: 운영 브랜치
- `develop`: 개발 통합 브랜치
- `feature/*`: 기능 개발
- `fix/*`: 버그 수정

### 4.2 커밋 메시지

```
type(scope): subject

body (optional)

footer (optional)
```

Types: feat, fix, docs, style, refactor, test, chore

예시:

```
feat(auth): implement JWT authentication

- Add login endpoint
- Add token refresh logic
- Update user model

Closes #123
```

## 5. 테스트

### 5.1 Backend 테스트 (pytest)

```bash
cd backend
pytest
pytest --cov=src tests/
```

### 5.2 Frontend 테스트 (Vitest)

```bash
cd frontend
pnpm test
pnpm test:coverage
```

## 6. API 개발 패턴

### 6.1 Directus 확장

[Directus Hook 및 Extension 개발 가이드]

### 6.2 Custom Backend API

```python
# routes/[feature].py
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models import [Model]
from src.services.[feature] import [Service]
from src.dependencies import get_db

router = APIRouter(prefix="/api/v1/[feature]", tags=["[feature]"])

@router.get("/")
async def list_items(
    db: AsyncSession = Depends(get_db)
) -> list[[Model]]:
    service = [Service](db)
    return await service.list()
```

## 7. 배포

[docs/06-DEPLOYMENT.md 참고]

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]

````

---

## 6. DEPLOYMENT (배포 가이드)

**파일명**: `docs/06-DEPLOYMENT.md`

```markdown
# [프로젝트명] - 배포 가이드

> 버전: 1.0 | 작성일: [날짜]

## 1. 환경 구성

### 1.1 환경 분리
- Development: 로컬 개발 환경
- Staging: 테스트 환경
- Production: 운영 환경

### 1.2 환경 변수

**공통**:
```bash
DATABASE_URL=mysql://user:password@host:3306/dbname
REDIS_URL=redis://host:6379
JWT_SECRET=your-secret-key
````

**환경별**:

```bash
# Development
NODE_ENV=development
API_URL=http://localhost:8055

# Production
NODE_ENV=production
API_URL=https://api.yourdomain.com
```

## 2. Docker 배포

### 2.1 Backend 이미지 빌드 (Custom Backend 사용 시)

```bash
cd backend
docker build -t [project]-backend:latest .
```

### 2.2 Docker Compose 실행

```bash
docker-compose up -d
# Directus, Redis, Backend(필요시)만 실행됨
```

### 2.3 Frontend 빌드 및 배포

```bash
# 빌드
cd frontend
pnpm install
pnpm build

# dist/ 디렉토리를 웹서버로 배포
# 방법 1: 직접 복사
cp -r dist/* /var/www/html/

# 방법 2: rsync
rsync -avz dist/ user@server:/var/www/html/

# 방법 3: CI/CD 파이프라인 사용
```

## 3. 운영 체크리스트

### 배포 전

- [ ] 모든 테스트 통과
- [ ] 환경 변수 설정 확인
- [ ] 데이터베이스 마이그레이션 준비
- [ ] 백업 수행

### 배포 중

- [ ] 무중단 배포 (필요시)
- [ ] 헬스 체크 확인
- [ ] 로그 모니터링

### 배포 후

- [ ] API 동작 확인
- [ ] Frontend 접속 확인
- [ ] 에러 모니터링
- [ ] 성능 메트릭 확인

## 4. Frontend 배포 (Nginx 예시)

### 4.1 Nginx 설정

```nginx
# /etc/nginx/sites-available/myproject
server {
    listen 80;
    server_name yourdomain.com;

    # Frontend 정적 파일
    root /var/www/html/myproject/dist;
    index index.html;

    # SPA 라우팅 처리
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API 프록시 (선택)
    location /api {
        proxy_pass http://localhost:8055;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # 캐싱 설정
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### 4.2 배포 스크립트

```bash
#!/bin/bash
# deploy-frontend.sh

set -e

echo "Building frontend..."
cd frontend
pnpm install
pnpm build

echo "Deploying to server..."
sudo rsync -avz --delete dist/ /var/www/html/myproject/dist/

echo "Reloading nginx..."
sudo nginx -t
sudo systemctl reload nginx

echo "Frontend deployed successfully!"
```

---

**문서 버전**: 1.0
**최종 업데이트**: [날짜]

````

---

## 7. MVP_CHECKLIST (MVP 체크리스트)

**파일명**: `docs/07-MVP_CHECKLIST.md`

```markdown
# [프로젝트명] - MVP 구현 체크리스트

> 버전: 1.0 | 작성일: [날짜]

이 체크리스트는 MVP를 단계적으로 구현하기 위한 가이드입니다.

## Phase 1: 환경 설정

### 1.1 Docker 환경
- [ ] docker-compose.yml 확인
- [ ] MySQL 컨테이너 실행 확인
- [ ] Directus 컨테이너 실행 확인 (사용 시)
- [ ] Redis 컨테이너 실행 확인 (사용 시)

### 1.2 Directus 초기 설정 (사용 시)
- [ ] 관리자 계정 생성
- [ ] [Collection 1] 생성
- [ ] [Collection 2] 생성
- [ ] 권한 설정
- [ ] API 토큰 발급

### 1.3 Backend 초기 설정 (Custom 사용 시)
- [ ] Python 가상 환경 설정
- [ ] 의존성 설치
- [ ] 데이터베이스 마이그레이션
- [ ] 서버 실행 확인

### 1.4 Frontend 초기 설정
- [ ] pnpm install
- [ ] 개발 서버 실행 확인
- [ ] Tailwind CSS 설정
- [ ] API 클라이언트 설정

### 1.5 Mobile 초기 설정
- [ ] pnpm install
- [ ] Expo 앱 실행 확인
- [ ] API 클라이언트 설정

## Phase 2: 인증 시스템

- [ ] 회원가입 API (Directus 기본 또는 Custom)
- [ ] 로그인 API
- [ ] 토큰 갱신 API
- [ ] 로그아웃 처리
- [ ] Frontend: 로그인 페이지
- [ ] Frontend: 회원가입 페이지
- [ ] Frontend: 인증 상태 관리
- [ ] Mobile: 로그인 화면
- [ ] Mobile: 회원가입 화면

## Phase 3: [핵심 기능 1]

[PRD의 첫 번째 핵심 기능을 위한 체크리스트]

### Backend
- [ ] 데이터 모델 정의 (Collection/SQLModel)
- [ ] CRUD API 구현
- [ ] 비즈니스 로직 구현
- [ ] 단위 테스트

### Frontend
- [ ] [기능] 목록 페이지
- [ ] [기능] 상세 페이지
- [ ] [기능] 생성 폼
- [ ] [기능] 수정 기능
- [ ] [기능] 삭제 기능

### Mobile
- [ ] [기능] 목록 화면
- [ ] [기능] 상세 화면
- [ ] [기능] 생성 화면

## Phase N: 통합 및 테스트

- [ ] API 통합 테스트
- [ ] E2E 테스트 (주요 플로우)
- [ ] 성능 테스트
- [ ] 보안 검토
- [ ] 문서 업데이트

## Phase N+1: 배포 준비

- [ ] 운영 환경 변수 설정
- [ ] Docker 이미지 빌드
- [ ] 배포 스크립트 작성
- [ ] 모니터링 설정
- [ ] 백업 전략 수립

---

**진행 상황**: [N] / [Total] 완료

**최종 업데이트**: [날짜]
````

---

## 템플릿 사용 가이드

1. **변수 치환**: `[...]`로 표시된 부분은 실제 프로젝트 정보로 치환
2. **IDEA.md 참조**: IDEA.md의 내용을 기반으로 확장
3. **선택적 섹션**: 프로젝트에 따라 불필요한 섹션은 제거
4. **코드 예시**: 실제 사용할 기술 스택에 맞춰 작성

---

**템플릿 버전**: 1.0.0
**업데이트**: 2026-01-28

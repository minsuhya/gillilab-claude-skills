---
name: idea-to-app
description: IDEA.md 파일로부터 전체 프로젝트 문서와 구조를 자동 생성하여 빠르게 구현까지 진행하는 풀스택 프로젝트 빌더. Directus+MySQL 기반 또는 Python 커스텀 백엔드, React 프론트엔드, Expo 모바일 앱 구조를 자동 생성합니다.
---

# idea-to-app 스킬

## 🎯 개요

IDEA.md 파일 하나로 시작하여 전체 프로젝트를 빠르게 구축하는 스킬입니다.

**핵심 가치:**

- ⚡ IDEA.md 작성 → 전체 문서 자동 생성 → 프로젝트 구조 생성 → 구현 가이드
- 🏗️ Directus + MySQL 기반 (또는 Python 커스텀 백엔드)
- 📱 React 프론트엔드 + Expo 모바일 앱
- 🐳 Docker Compose 기반 개발/운영 환경
- ✅ 단계별 사용자 확인 및 피드백

## 🚀 실행 방법

```bash
# 프로젝트 디렉토리에서
/idea-to-app
```

또는 인자와 함께:

```bash
/idea-to-app --skip-questions  # 대화형 질문 생략
```

## 📋 전제 조건

실행 전 확인사항:

1. 프로젝트 루트 디렉토리에 `IDEA.md` 파일이 존재해야 함
2. IDEA.md에 최소한 다음 정보가 포함되어야 함:
   - 프로젝트명
   - 한 줄 소개
   - 핵심 기능 (최소 3개)

만약 IDEA.md가 없다면:

- **[IDEA_TEMPLATE.md](./IDEA_TEMPLATE.md)**를 참고하여 먼저 작성하도록 안내
- 템플릿을 사용자 프로젝트에 복사하여 작성 시작

## 🔄 실행 프로세스

### Phase 0: 초기 확인 및 분석

1. **IDEA.md 존재 여부 확인**
   - 없으면: 템플릿 제공 및 작성 가이드
   - 있으면: 내용 분석 시작

2. **IDEA.md 내용 분석**
   - 프로젝트명 추출
   - 핵심 기능 파악
   - 기술 스택 확인 (명시되지 않았다면 기본 스택 사용)
   - 특별 요구사항 파악

3. **사용자 확인 (선택적)**

   ```
   분석 결과:
   - 프로젝트명: [추출된 이름]
   - 핵심 기능: [N개]
   - 기술 스택: [기본/커스텀]

   이 내용으로 진행할까요? (Y/n)
   ```

### Phase 1: 문서 생성

다음 순서로 문서를 생성합니다. 각 문서 생성 후 간단히 사용자에게 확인을 구합니다.

#### 1.1 docs/ 디렉토리 생성

```bash
mkdir -p docs docs/policies
```

#### 1.2 PRD (제품 요구사항 정의서) 생성

- **파일**: `docs/01-PRD.md`
- **내용**: [templates.md의 PRD 템플릿 참고]
- **확인 포인트**: 핵심 기능이 모두 포함되었는지

#### 1.3 Architecture (시스템 아키텍처) 생성

- **파일**: `docs/02-ARCHITECTURE.md`
- **내용**: [templates.md의 Architecture 템플릿 참고]
- **기술 스택 결정**:
  - 기본: Directus + MySQL
  - 커스텀 로직 필요 시: Python (FastAPI + SQLModel + Pydantic) 추가
- **확인 포인트**: 기술 스택이 요구사항을 충족하는지

#### 1.4 API Spec (API 명세서) 생성

- **파일**: `docs/03-API_SPEC.md`
- **내용**: [templates.md의 API Spec 템플릿 참고]
- **Directus 사용 시**: Directus 기본 API 명세 + 커스텀 엔드포인트
- **확인 포인트**: 모든 기능에 대한 API가 정의되었는지

#### 1.5 Database Schema (DB 스키마) 생성

- **파일**: `docs/04-DATABASE_SCHEMA.md`
- **내용**: [templates.md의 Database Schema 템플릿 참고]
- **Directus 사용 시**: Directus Collections 정의 포함
- **확인 포인트**: 데이터 모델이 기능을 지원하는지

#### 1.6 Development Guide (개발 가이드) 생성

- **파일**: `docs/05-DEVELOPMENT_GUIDE.md`
- **내용**: [templates.md의 Development Guide 템플릿 참고]
- **포함 사항**:
  - 개발 환경 설정
  - 프로젝트 구조
  - 코딩 컨벤션
  - 테스트 전략

#### 1.7 Deployment Guide (배포 가이드) 생성

- **파일**: `docs/06-DEPLOYMENT.md`
- **내용**: Docker 기반 배포 가이드

#### 1.8 MVP Checklist (MVP 체크리스트) 생성

- **파일**: `docs/07-MVP_CHECKLIST.md`
- **내용**: 단계별 구현 체크리스트

#### 1.9 README.md 생성/업데이트

- **파일**: `README.md`
- **내용**: 프로젝트 소개 및 시작 가이드

### Phase 2: 프로젝트 구조 생성

사용자에게 확인 후 프로젝트 디렉토리 구조를 생성합니다.

```
프로젝트 디렉토리 구조를 생성할까요? (Y/n)
```

#### 2.1 Docker 설정 생성

```bash
# docker-compose.yml 생성
# .docker/ 마운트 디렉토리 생성
mkdir -p .docker/mysql .docker/directus .docker/redis
```

**docker-compose.yml 내용**:

- Directus 서비스 (외부 MySQL에 연결)
- Redis 서비스
- Custom Backend 서비스 (필요 시, 외부 MySQL에 연결)
- MySQL 서비스 (주석 처리, 로컬 개발 필요 시 활성화)

##### 2.1.1 Backend 구성 전략

**MySQL: 외부 통합 기본**
- AWS RDS, Azure Database, 자체 MySQL 서버 등 외부 MySQL 사용 권장
- 환경 변수로 연결 정보만 제공 (DATABASE_URL)
- 로컬 개발용 MySQL이 필요한 경우에만 docker-compose.yml에 추가 (주석 처리된 예시 제공)

**Backend 옵션**:
1. **Directus만 사용** (기본 CRUD)
   - 외부 MySQL 연동
   - Directus만 Docker Compose로 실행

2. **Directus + Python Backend** (커스텀 로직 필요 시)
   - Directus: 기본 데이터 관리
   - Python (FastAPI + SQLModel + Pydantic): 복잡한 비즈니스 로직
   - 둘 다 외부 MySQL에 연결

#### 2.2 환경 변수 파일 생성

```bash
# .env.example 생성
```

#### 2.3 Backend 디렉토리 생성 (커스텀 백엔드 사용 시)

```
backend/
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── pytest.ini
└── src/
    ├── main.py
    ├── config.py
    ├── models/
    ├── routes/
    ├── services/
    └── utils/
```

#### 2.4 Frontend 디렉토리 생성

```
frontend/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── index.html
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── pages/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── types/
└── public/

# 빌드 후 생성 (운영 배포용)
dist/                # pnpm build 실행 시 생성
├── index.html
├── assets/
└── ...
```

**배포 방법**:
```bash
# 빌드
cd frontend
pnpm build

# dist/ 디렉토리를 Host Nginx/Apache 등으로 배포
# 예: /var/www/html 또는 /usr/share/nginx/html
```

#### 2.5 Mobile 디렉토리 생성

```
mobile/
├── package.json
├── app.json
├── tsconfig.json
├── app/
│   ├── _layout.tsx
│   ├── index.tsx
│   └── (tabs)/
├── components/
├── hooks/
├── lib/
└── assets/
```

### Phase 3: 구현 가이드 제시

프로젝트 구조 생성 후, 다음 단계를 안내합니다:

```
✅ 문서 생성 완료
✅ 프로젝트 구조 생성 완료

📚 생성된 문서:
- docs/01-PRD.md
- docs/02-ARCHITECTURE.md
- docs/03-API_SPEC.md
- docs/04-DATABASE_SCHEMA.md
- docs/05-DEVELOPMENT_GUIDE.md
- docs/06-DEPLOYMENT.md
- docs/07-MVP_CHECKLIST.md

🏗️ 생성된 구조:
- docker-compose.yml
- backend/ (필요 시)
- frontend/
- mobile/

🚀 다음 단계:

1. 외부 MySQL 준비
   - AWS RDS, Azure Database 등 MySQL 인스턴스 생성
   - 또는 기존 MySQL 서버 사용
   - 데이터베이스 생성 및 사용자 권한 설정

2. 환경 변수 설정
   cp .env.example .env
   # .env 파일에서 DB_HOST, DB_USER, DB_PASSWORD 등 외부 MySQL 정보 입력

3. Docker 서비스 시작
   docker-compose up -d
   # Directus와 Redis만 실행됨 (MySQL은 외부 서버 사용)

4. Directus 초기 설정
   - http://localhost:8055 접속
   - 관리자 계정 생성 (이미 .env에 설정한 경우 자동)
   - Collection 생성 (docs/04-DATABASE_SCHEMA.md 참고)

5. Frontend 개발 시작
   cd frontend
   pnpm install
   pnpm dev

6. Mobile 개발 시작
   cd mobile
   pnpm install
   pnpm start # or npx expo start --clear

구현을 시작할까요? 어떤 부분부터 진행하고 싶으신가요?
- [1] Directus Collection 설정
- [2] Frontend 기본 구조 구현
- [3] Mobile 기본 구조 구현
- [4] Custom Backend API 구현 (필요 시)
```

### Phase 4: 구현 지원 (선택)

사용자가 요청하면 실제 구현을 단계별로 진행합니다.

#### 4.1 Directus Collection 설정

- docs/04-DATABASE_SCHEMA.md 기반으로 Collection 정의
- JSON 스키마 제공 (Directus import 가능)

#### 4.2 Frontend 구현

- 기본 라우팅 설정
- API 클라이언트 설정
- 주요 페이지 스캐폴딩

#### 4.3 Mobile 구현

- 기본 네비게이션 설정
- API 클라이언트 설정
- 주요 화면 스캐폴딩

#### 4.4 Custom Backend 구현

- FastAPI 기본 설정
- SQLModel 모델 정의
- 라우터 및 서비스 레이어 구현

### Phase 5: 테스트 및 검증

구현 완료 후:

- [ ] Docker 서비스 정상 실행 확인
- [ ] API 엔드포인트 테스트
- [ ] Frontend 로컬 실행 확인
- [ ] Mobile 앱 실행 확인
- [ ] 문서와 구현 일치 여부 확인

## 🎨 기본 기술 스택

### Backend

- **Database**: MySQL 8.0 (외부 통합 권장 - AWS RDS, Azure Database 등)
- **CMS/API**: Directus (기본, Docker Compose로 실행)
- **Custom Backend**: Python 3.11 + FastAPI + SQLModel + Pydantic (선택, Docker Compose로 실행)
- **Cache**: Redis (Docker Compose로 실행)

### Frontend

- **Framework**: React 19 + TypeScript
- **Build Tool**: Vite 7
- **Package Manager**: pnpm
- **UI Library**: Tailwind CSS v4
- **State Management**: React Query + Zustand 5
- **Form**: React Hook Form + Zod
- **개발 환경**: pnpm dev (로컬 개발 서버, http://localhost:5173)
- **운영 환경**: pnpm build → dist/ 생성 → Host Nginx/Apache 등으로 서빙
  - Docker 컨테이너 사용 안 함
  - 정적 파일로 배포

### Mobile

- **Framework**: Expo SDK 54
- **Language**: React Native 0.81 + TypeScript
- **Navigation**: Expo Router 6
- **UI**: NativeWind v4 (Tailwind CSS for React Native)
  - ⚠️ NativeWind v4는 Tailwind CSS v3 기반 (Frontend의 v4와 다름)
  - 필수 설정: babel.config.js, metro.config.js, tailwind.config.js, global.css

### DevOps

- **Container**: Docker + Docker Compose
- **Environment**: .env 기반 설정

## 📝 문서 생성 규칙

### 파일명 규칙

- 숫자 접두사 + 대문자 시작 + 언더스코어
- 예: `01-PRD.md`, `02-ARCHITECTURE.md`

### 내용 규칙

- 모든 문서는 한국어로 작성
- 코드 예시는 실제 사용할 기술 스택에 맞춤
- 문서 간 상호 참조 사용 (중복 방지)
- 실행 가능한 수준의 상세함

### 체크리스트 규칙

- 구체적이고 실행 가능한 항목
- Phase별로 그룹화
- 의존성 표시

## 🔧 커스터마이징

### 기술 스택 변경

IDEA.md에 다음과 같이 명시:

```markdown
## 기술 스택

- Backend: Python (FastAPI + SQLModel)
- Frontend: Next.js
- Mobile: Flutter
```

### 추가 서비스

docker-compose.yml에 자동 추가되는 서비스:

- AI 기능 필요 시: Python backend 자동 추가
- 실시간 기능: Redis 자동 추가
- 파일 저장: MinIO 또는 S3 설정 추가

## ⚠️ 주의사항

1. **기존 파일 보호**
   - 이미 존재하는 파일은 덮어쓰지 않음
   - 사용자에게 확인 후 진행

2. **단계별 확인**
   - 각 Phase 완료 후 사용자 확인
   - 문제 발생 시 되돌리기 가능

3. **Directus vs Custom Backend**
   - 기본은 Directus 권장
   - 복잡한 비즈니스 로직 필요 시 Custom Backend
   - 두 개를 함께 사용 가능 (하이브리드)

4. **환경 변수**
   - 민감한 정보는 .env에만 저장
   - .env.example에는 예시 값만

## 📚 관련 파일

- [IDEA_TEMPLATE.md](./IDEA_TEMPLATE.md): IDEA.md 작성 템플릿
- [templates.md](./templates.md): 문서 템플릿 전체 (PRD, Architecture 등)
- [project-templates.md](./project-templates.md): 프로젝트 구조 템플릿 (docker-compose, backend, frontend, mobile)
- [examples.md](./examples.md): 실제 사용 예시

## 🎯 성공 기준

스킬 실행 완료 후:

- ✅ 모든 문서가 생성됨
- ✅ 프로젝트 구조가 올바르게 생성됨
- ✅ docker-compose up으로 환경이 실행됨
- ✅ 문서를 따라가면 구현 가능한 수준
- ✅ MVP 체크리스트가 구체적이고 실행 가능함

## 🚀 버전 정보

- **버전**: 1.0.0
- **업데이트**: 2026-01-28
- **호환성**: Claude Code v1.0+

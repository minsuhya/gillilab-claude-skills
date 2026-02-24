# 서브 에이전트 조율 가이드

## 서브 에이전트 개요

풀스택 개발을 위해 4개의 서브 에이전트가 있습니다:

### 1. frontend-agent
- **역할**: React UI 개발
- **입력**: UI 요구사항, 디자인 명세
- **출력**: HTML/React 코드

### 2. backend-agent
- **역할**: Flask API 개발
- **입력**: API 명세, 비즈니스 로직
- **출력**: Python Flask 코드

### 3. database-agent
- **역할**: 데이터베이스 설계
- **입력**: 데이터 모델 요구사항
- **출력**: SQL 스키마, SQLAlchemy 모델

### 4. testing-agent
- **역할**: 테스트 코드 작성
- **입력**: 전체 코드베이스
- **출력**: Pytest 테스트, 테스트 체크리스트

## 조율 전략

### 순차적 실행 (Sequential)
데이터베이스 → 백엔드 → 프론트엔드 → 테스팅

**사용 시기**: 각 단계가 이전 단계에 의존하는 경우

**예시**:
1. database-agent: 데이터 모델 설계
2. backend-agent: 데이터 모델 기반 API 구현
3. frontend-agent: API 기반 UI 구현
4. testing-agent: 전체 코드 테스트

### 병렬 실행 (Parallel)
명확히 분리된 작업을 동시 진행

**사용 시기**: 독립적인 작업이 있는 경우

**예시**:
- frontend-agent + backend-agent를 동시에 (API 명세만 공유)
- 완료 후 database-agent, testing-agent 진행

### 반복적 실행 (Iterative)
피드백을 통한 점진적 개선

**사용 시기**: 요구사항이 불명확하거나 프로토타입 필요시

**예시**:
1. 기본 버전 생성 (모든 에이전트)
2. 사용자 피드백 수집
3. 각 에이전트별 개선 작업
4. 반복

## 에이전트 간 통신

### 정보 전달 형식

#### Database → Backend
```python
{
    "models": ["User", "Item", "Tag"],
    "relationships": {
        "User-Item": "one-to-many",
        "Item-Tag": "many-to-many"
    },
    "schema_file": "schema.sql",
    "models_file": "models.py"
}
```

#### Backend → Frontend
```javascript
{
    "endpoints": [
        {"method": "GET", "path": "/api/items", "response": "List[Item]"},
        {"method": "POST", "path": "/api/items", "request": "Item", "response": "Item"}
    ],
    "data_models": {
        "Item": {
            "id": "number",
            "title": "string",
            "description": "string"
        }
    }
}
```

#### All → Testing
```python
{
    "frontend_files": ["frontend.html"],
    "backend_files": ["backend.py"],
    "database_files": ["models.py"],
    "test_priority": ["api_endpoints", "data_models", "ui_functionality"]
}
```

## 충돌 해결

### 스키마 변경 필요시
1. database-agent가 스키마 수정
2. backend-agent가 모델 업데이트
3. frontend-agent가 UI 조정
4. testing-agent가 테스트 업데이트

### API 엔드포인트 변경시
1. backend-agent가 엔드포인트 수정
2. frontend-agent가 API 호출 코드 수정
3. testing-agent가 관련 테스트 업데이트

## 품질 체크포인트

각 단계마다 확인:
- [ ] 요구사항 충족
- [ ] 에이전트 간 인터페이스 일치
- [ ] 코드 품질 기준 달성
- [ ] 문서화 완료


---

# 풀스택 구현 데모 예시

## 📝 사용자 요청

```
fullstack-orchestrator 스킬을 사용해서 할일 관리 웹앱을 만들어줘.

요구사항:
- 사용자가 할일을 추가, 수정, 삭제, 완료 표시할 수 있어야 함
- 할일은 제목, 설명, 상태(진행중/완료), 생성일자를 가짐
- 깔끔한 UI로 모든 할일 목록을 볼 수 있어야 함
- 완료된 할일은 회색으로 표시
```

---

## 🤖 메인 에이전트 (fullstack-orchestrator) 실행

### Phase 1: 요구사항 분석
```
분석 결과:
✓ 데이터 모델: Todo (id, title, description, status, created_at)
✓ API 엔드포인트: CRUD + 완료 표시
✓ UI 요구사항: 목록 표시, 추가/수정 폼, 완료 토글
✓ 기술 스택: SQLite, Flask, React
```

### Phase 2: 작업 계획
```
실행 순서 (순차):
1. database-agent → 데이터 스키마 및 모델
2. backend-agent → Flask API
3. frontend-agent → React UI
4. testing-agent → 테스트 코드
```

---

## 🗄️ 서브 에이전트 1: database-agent

### 입력 (메인 → Database)
```json
{
  "entities": ["Todo"],
  "fields": {
    "Todo": {
      "id": "INTEGER PRIMARY KEY",
      "title": "VARCHAR(200) NOT NULL",
      "description": "TEXT",
      "status": "VARCHAR(20) DEFAULT 'pending'",
      "created_at": "TIMESTAMP"
    }
  }
}
```

### 출력 (Database → 메인)
```
생성된 파일:
1. schema.sql - 데이터베이스 스키마
2. models.py - SQLAlchemy 모델

주요 내용:
- Todo 테이블 정의
- status 인덱스
- to_dict() 메서드
```

---

## 🔧 서브 에이전트 2: backend-agent

### 입력 (메인 → Backend)
```json
{
  "endpoints": [
    {"method": "GET", "path": "/api/todos", "description": "모든 할일 조회"},
    {"method": "POST", "path": "/api/todos", "description": "할일 생성"},
    {"method": "PUT", "path": "/api/todos/:id", "description": "할일 수정"},
    {"method": "DELETE", "path": "/api/todos/:id", "description": "할일 삭제"},
    {"method": "PATCH", "path": "/api/todos/:id/complete", "description": "완료 표시"}
  ],
  "models": "models.py"
}
```

### 출력 (Backend → 메인)
```
생성된 파일:
1. app.py - Flask 서버
2. requirements.txt

API 엔드포인트:
✓ GET /api/todos - 200 OK
✓ POST /api/todos - 201 Created
✓ PUT /api/todos/:id - 200 OK
✓ DELETE /api/todos/:id - 200 OK
✓ PATCH /api/todos/:id/complete - 200 OK
```

---

## 🎨 서브 에이전트 3: frontend-agent

### 입력 (메인 → Frontend)
```json
{
  "api_endpoints": [
    "GET /api/todos",
    "POST /api/todos",
    "PUT /api/todos/:id",
    "DELETE /api/todos/:id",
    "PATCH /api/todos/:id/complete"
  ],
  "data_model": {
    "Todo": {
      "id": "number",
      "title": "string",
      "description": "string",
      "status": "string",
      "created_at": "string"
    }
  },
  "ui_requirements": "할일 목록, 추가 폼, 완료 토글, 완료된 항목 회색 표시"
}
```

### 출력 (Frontend → 메인)
```
생성된 파일:
1. frontend.html - React UI

주요 컴포넌트:
✓ TodoList - 할일 목록 표시
✓ TodoForm - 추가/수정 폼
✓ TodoItem - 개별 할일 아이템
✓ 완료 토글 버튼
✓ Tailwind CSS 스타일링
```

---

## 🧪 서브 에이전트 4: testing-agent

### 입력 (메인 → Testing)
```json
{
  "files": ["app.py", "models.py", "frontend.html"],
  "test_scope": [
    "API 엔드포인트",
    "데이터 모델",
    "UI 기능"
  ]
}
```

### 출력 (Testing → 메인)
```
생성된 파일:
1. test_backend.py - 백엔드 테스트 (pytest)
2. frontend_test_checklist.md - 프론트엔드 테스트

테스트 커버리지:
✓ API 엔드포인트: 100%
✓ CRUD 작업: 100%
✓ 에러 처리: 100%
✓ UI 체크리스트: 완료
```

---

## 📦 최종 산출물

### 파일 목록
```
todo-app/
├── schema.sql              # 데이터베이스 스키마
├── models.py              # SQLAlchemy 모델
├── app.py                 # Flask API 서버
├── frontend.html          # React UI
├── test_backend.py        # 백엔드 테스트
├── frontend_test.md       # 프론트엔드 테스트
├── requirements.txt       # Python 의존성
├── README.md             # 프로젝트 설명
└── SETUP.md              # 설치 및 실행 가이드
```

### 설치 및 실행

#### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

#### 2. 데이터베이스 초기화
```bash
python models.py
```

#### 3. 백엔드 서버 실행
```bash
python app.py
# 서버가 http://localhost:5000 에서 실행됨
```

#### 4. 프론트엔드 실행
```bash
# frontend.html을 브라우저에서 열기
open frontend.html
```

#### 5. 테스트 실행
```bash
pytest test_backend.py -v
```

---

## 🎯 결과 요약

### 메인 에이전트의 역할
```
✓ 요구사항 분석 및 분해
✓ 4개 서브 에이전트에 작업 위임
✓ 각 에이전트 출력물 검증
✓ 호환성 확인 및 통합
✓ 문서화 및 최종 전달
```

### 개발 시간
```
전통적 방식: 4-6시간
에이전트 시스템: 5-10분
```

### 코드 품질
```
✓ RESTful API 설계
✓ 적절한 데이터 모델링
✓ 반응형 UI
✓ 테스트 코드 포함
✓ 문서화 완료
```

---

## 💡 추가 개선 예시

### 프롬프트:
```
위 할일 앱에서 frontend-agent를 사용해서 
다크모드 기능을 추가해줘.
```

### 프롬프트:
```
backend-agent를 사용해서 
할일에 우선순위(높음/중간/낮음) 필드를 추가하고
우선순위별로 정렬하는 API를 추가해줘.
```

### 프롬프트:
```
database-agent를 사용해서 
User 테이블을 추가하고 Todo와 1:N 관계를 설정해줘.
```

---

## 📊 에이전트 간 통신 흐름도

```
사용자 요청
    ↓
[fullstack-orchestrator]
    ↓
    ├─→ [database-agent] → schema.sql, models.py
    │                          ↓
    ├─→ [backend-agent] ←──────┘ → app.py, requirements.txt
    │                          ↓
    ├─→ [frontend-agent] ←─────┘ → frontend.html
    │                          ↓
    └─→ [testing-agent] ←──────┘ → test_backend.py, frontend_test.md
                                ↓
                           [통합 및 검증]
                                ↓
                           최종 산출물
```

---

## ✅ 체크리스트

작업 완료 확인:
- [x] 데이터베이스 스키마 생성
- [x] API 엔드포인트 구현
- [x] 프론트엔드 UI 생성
- [x] 테스트 코드 작성
- [x] 문서화 완료
- [x] 코드 호환성 검증
- [x] 실행 가능한 상태

---

## 🚀 다음 단계

1. **로컬에서 실행**: 생성된 코드를 다운로드하여 실행
2. **커스터마이징**: 필요에 따라 코드 수정
3. **배포 준비**: 프로덕션 환경 설정 추가
4. **확장**: 추가 기능 개발 (위의 개선 예시 참조)

Happy Coding! 🎉


---

# 풀스택 에이전트 시스템 가이드

## 📚 개요

이 시스템은 Claude Skills를 활용한 **메인/서브 에이전트 아키텍처**로 풀스택 웹 애플리케이션을 개발합니다.

### 에이전트 구조

```
fullstack-orchestrator (메인 에이전트)
├─ frontend-agent (프론트엔드 서브 에이전트)
├─ backend-agent (백엔드 서브 에이전트)
├─ database-agent (데이터베이스 서브 에이전트)
└─ testing-agent (테스팅 서브 에이전트)
```

## 📦 스킬 설치

### 1단계: 모든 스킬 다운로드
다음 5개의 `.skill` 파일을 다운로드하세요:
- `fullstack-orchestrator.skill` (메인 에이전트)
- `frontend-agent.skill`
- `backend-agent.skill`
- `database-agent.skill`
- `testing-agent.skill`

### 2단계: Claude에 업로드
1. Claude 설정 → Skills로 이동
2. 5개의 스킬 파일을 모두 업로드
3. 각 스킬이 활성화되었는지 확인

## 🚀 사용 예시

### 예시 1: 할일 관리 앱 만들기

#### 사용자 프롬프트:
```
fullstack-orchestrator 스킬을 사용해서 할일 관리 웹앱을 만들어줘.

요구사항:
- 사용자가 할일을 추가, 수정, 삭제, 완료 표시할 수 있어야 함
- 할일은 제목, 설명, 상태(진행중/완료), 생성일자를 가짐
- 깔끔한 UI로 모든 할일 목록을 볼 수 있어야 함
- 완료된 할일은 회색으로 표시
```

#### Claude의 처리 과정:

**Phase 1: 요구사항 분석**
```
메인 에이전트(fullstack-orchestrator)가 분석:
- 데이터 모델: Todo (id, title, description, status, created_at)
- API 엔드포인트: CRUD 작업
- UI: 할일 목록, 추가 폼, 수정/삭제 버튼
```

**Phase 2: Database Agent 실행**
```
database-agent 스킬을 사용하여 다음을 생성:

1. schema.sql
   - todos 테이블 정의
   - 필요한 인덱스

2. models.py
   - SQLAlchemy Todo 모델
   - to_dict() 메서드
```

**Phase 3: Backend Agent 실행**
```
backend-agent 스킬을 사용하여 다음을 생성:

1. app.py (Flask API)
   - GET /api/todos - 모든 할일 조회
   - POST /api/todos - 할일 생성
   - PUT /api/todos/:id - 할일 수정
   - DELETE /api/todos/:id - 할일 삭제
   - PATCH /api/todos/:id/complete - 완료 표시

2. requirements.txt
   - Flask, Flask-CORS, SQLAlchemy
```

**Phase 4: Frontend Agent 실행**
```
frontend-agent 스킬을 사용하여 다음을 생성:

1. frontend.html
   - React 컴포넌트 구조
   - 할일 목록 표시
   - 추가/수정/삭제 기능
   - 완료 표시 기능
   - Tailwind CSS 스타일링
```

**Phase 5: Testing Agent 실행**
```
testing-agent 스킬을 사용하여 다음을 생성:

1. test_backend.py
   - API 엔드포인트 테스트
   - CRUD 작업 테스트
   - 에러 처리 테스트

2. frontend_test_checklist.md
   - 수동 테스트 체크리스트
   - 반응형 테스트 가이드
```

**Phase 6: 통합 및 문서화**
```
메인 에이전트가 최종 산출물 제공:
- 모든 코드 파일
- README.md (프로젝트 설명)
- SETUP.md (설치 및 실행 가이드)
```

### 예시 2: 블로그 플랫폼 만들기

#### 사용자 프롬프트:
```
fullstack-orchestrator를 사용해서 간단한 블로그 플랫폼을 만들어줘.

요구사항:
- 사용자는 글을 작성, 수정, 삭제할 수 있음
- 글은 제목, 내용, 작성자, 태그를 가짐
- 태그로 글을 필터링할 수 있음
- 최신 글부터 보여주는 UI
```

#### 예상 결과물:
1. **Database**: User, Post, Tag 테이블 + 관계 설정
2. **Backend**: 사용자 인증, 글 CRUD, 태그 필터링 API
3. **Frontend**: 글 목록, 작성/수정 폼, 태그 필터
4. **Testing**: 전체 기능 테스트 코드

## 💡 프롬프트 작성 팁

### ✅ 좋은 프롬프트
```
fullstack-orchestrator를 사용해서 [앱 이름]을(를) 만들어줘.

요구사항:
- [기능 1]: [구체적 설명]
- [기능 2]: [구체적 설명]
- [UI 요구사항]
- [특별한 제약사항]
```

### ❌ 나쁜 프롬프트
```
웹앱 만들어줘  // 너무 모호함
```

## 🔧 고급 사용법

### 단계별 실행
특정 에이전트만 사용하고 싶다면:

```
# 데이터베이스만 먼저 설계
database-agent를 사용해서 블로그 플랫폼의 데이터베이스를 설계해줘.

# 그 다음 백엔드
backend-agent를 사용해서 위에서 만든 데이터베이스 기반으로 API를 만들어줘.
```

### 병렬 실행 요청
```
fullstack-orchestrator를 사용하되, 
프론트엔드와 백엔드를 병렬로 개발해줘. 
API 명세는 미리 정의해서 공유하고.
```

### 반복 개선
```
위에서 만든 할일 앱에서 frontend-agent를 사용해서 
UI를 더 현대적인 디자인으로 개선해줘.
```

## 📊 결과물 예시

### 디렉토리 구조
```
todo-app/
├── frontend.html          # React UI
├── app.py                # Flask API
├── models.py             # SQLAlchemy 모델
├── schema.sql            # DB 스키마
├── test_backend.py       # 백엔드 테스트
├── frontend_test.md      # 프론트엔드 테스트
├── requirements.txt      # Python 의존성
├── README.md            # 프로젝트 문서
└── SETUP.md             # 설치 가이드
```

### 실행 방법
```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 데이터베이스 초기화
python models.py

# 3. 백엔드 실행
python app.py

# 4. 브라우저에서 frontend.html 열기
```

## 🎯 활용 시나리오

### 1. 프로토타입 개발
- 빠른 MVP 생성
- 아이디어 검증
- 데모 준비

### 2. 학습 목적
- 풀스택 개발 패턴 학습
- 각 레이어별 코드 이해
- 베스트 프랙티스 습득

### 3. 코드 스캐폴딩
- 프로젝트 초기 구조 생성
- 보일러플레이트 코드 자동화
- 이후 수동으로 커스터마이징

### 4. 레거시 현대화
- 기존 앱의 구조 분석
- 현대적 스택으로 재작성
- 단계별 마이그레이션

## ⚠️ 제한사항

### 1. 복잡한 비즈니스 로직
- 매우 복잡한 로직은 수동 작업 필요
- 에이전트는 일반적인 패턴에 최적화

### 2. 프로덕션 배포
- 생성된 코드는 기본 구조
- 보안, 성능 최적화는 추가 작업 필요
- 프로덕션 배포 전 검토 필수

### 3. 대규모 프로젝트
- 중소규모 프로젝트에 적합
- 대규모는 여러 번 나누어 작업

## 🔍 트러블슈팅

### Q1: 에이전트가 작동하지 않아요
A: 모든 5개 스킬이 업로드되고 활성화되었는지 확인하세요.

### Q2: 코드가 서로 호환되지 않아요
A: fullstack-orchestrator가 통합을 담당합니다. 메인 에이전트를 통해 실행하세요.

### Q3: 특정 기능만 수정하고 싶어요
A: 해당 서브 에이전트만 직접 호출하여 수정 작업을 진행하세요.

## 📖 추가 학습 자료

### 각 스킬의 상세 내용
- `frontend-agent`: React, Tailwind CSS 패턴
- `backend-agent`: Flask API, RESTful 설계
- `database-agent`: SQLAlchemy, 관계 설계
- `testing-agent`: Pytest, 테스트 전략

### 권장 학습 순서
1. 간단한 앱부터 시작 (할일 앱 등)
2. 각 에이전트의 출력물 분석
3. 점진적으로 복잡도 증가
4. 필요시 수동 커스터마이징

---

## 🎉 시작하기

1. 5개 스킬을 모두 Claude에 업로드
2. 간단한 프롬프트로 시작:
   ```
   fullstack-orchestrator를 사용해서 
   간단한 메모 앱을 만들어줘.
   ```
3. 결과를 확인하고 필요시 수정 요청
4. 생성된 코드를 로컬에서 실행

Happy Coding! 🚀

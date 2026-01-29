# idea-to-app 프로젝트 구조 템플릿

이 파일은 스킬이 생성하는 프로젝트 구조의 모든 파일 템플릿을 포함합니다.

---

## 루트 파일

### docker-compose.yml

**경로**: `docker-compose.yml`

```yaml
version: '3.8'

# 외부 MySQL 사용 권장: AWS RDS, Azure Database, 자체 MySQL 서버 등
# 로컬 개발용 MySQL이 필요한 경우 아래 mysql 서비스 주석 해제

services:
  # MySQL Database (로컬 개발용 - 선택 사항)
  # 프로덕션에서는 외부 MySQL 사용 권장 (AWS RDS, Azure Database 등)
  # mysql:
  #   image: mysql:8.0
  #   container_name: ${PROJECT_NAME:-myproject}-mysql
  #   environment:
  #     MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD:-rootpassword}
  #     MYSQL_DATABASE: ${DB_DATABASE:-myapp}
  #     MYSQL_USER: ${DB_USER:-user}
  #     MYSQL_PASSWORD: ${DB_PASSWORD:-password}
  #   volumes:
  #     - ./.docker/mysql:/var/lib/mysql
  #   ports:
  #     - "${DB_PORT:-3306}:3306"
  #   restart: unless-stopped
  #   networks:
  #     - app-network

  # Directus CMS (기본 API로 사용)
  # 외부 MySQL에 연결
  directus:
    image: directus/directus:latest
    container_name: ${PROJECT_NAME:-myproject}-directus
    environment:
      KEY: ${DIRECTUS_KEY:-replace-with-random-value}
      SECRET: ${DIRECTUS_SECRET:-replace-with-random-secret}

      # 외부 MySQL 연결 정보
      DB_CLIENT: mysql
      DB_HOST: ${DB_HOST}                    # 외부 MySQL 호스트
      DB_PORT: ${DB_PORT:-3306}
      DB_DATABASE: ${DB_DATABASE}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}

      # Admin Account
      ADMIN_EMAIL: ${DIRECTUS_ADMIN_EMAIL:-admin@example.com}
      ADMIN_PASSWORD: ${DIRECTUS_ADMIN_PASSWORD:-admin}

      # Cache (Redis)
      CACHE_ENABLED: ${CACHE_ENABLED:-true}
      CACHE_STORE: redis
      CACHE_REDIS: redis://redis:6379

      # Other
      PUBLIC_URL: ${DIRECTUS_PUBLIC_URL:-http://localhost:8055}
      CORS_ENABLED: true
      CORS_ORIGIN: ${CORS_ORIGIN:-*}
    volumes:
      - ./.docker/directus/uploads:/directus/uploads
      - ./.docker/directus/extensions:/directus/extensions
    ports:
      - "${DIRECTUS_PORT:-8055}:8055"
    depends_on:
      - redis
      # 로컬 MySQL 사용 시 주석 해제
      # - mysql
    restart: unless-stopped
    networks:
      - app-network

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: ${PROJECT_NAME:-myproject}-redis
    volumes:
      - ./.docker/redis:/data
    ports:
      - "${REDIS_PORT:-6379}:6379"
    restart: unless-stopped
    networks:
      - app-network
    command: redis-server --appendonly yes

  # Custom Backend (Python FastAPI) - 커스텀 로직 필요 시
  # backend 디렉토리가 있을 때 주석 해제
  # backend:
  #   build:
  #     context: ./backend
  #     dockerfile: Dockerfile
  #   container_name: ${PROJECT_NAME:-myproject}-backend
  #   environment:
  #     # 외부 MySQL 연결
  #     DATABASE_URL: mysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}
  #     REDIS_URL: redis://redis:6379
  #     JWT_SECRET: ${JWT_SECRET}
  #     ENVIRONMENT: ${ENVIRONMENT:-development}
  #   volumes:
  #     - ./backend:/app
  #   ports:
  #     - "${BACKEND_PORT:-8000}:8000"
  #   depends_on:
  #     - redis
  #   restart: unless-stopped
  #   networks:
  #     - app-network
  #   command: uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

  # Celery Worker (비동기 작업) - 필요 시
  # celery-worker:
  #   build:
  #     context: ./backend
  #     dockerfile: Dockerfile
  #   container_name: ${PROJECT_NAME:-myproject}-celery-worker
  #   environment:
  #     DATABASE_URL: mysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}
  #     REDIS_URL: redis://redis:6379
  #   volumes:
  #     - ./backend:/app
  #   depends_on:
  #     - redis
  #   restart: unless-stopped
  #   networks:
  #     - app-network
  #   command: celery -A src.celery_app worker --loglevel=info

networks:
  app-network:
    driver: bridge
```

---

### .env.example

**경로**: `.env.example`

```bash
# Project
PROJECT_NAME=myproject
ENVIRONMENT=development

# ===== 외부 MySQL 연결 정보 (필수) =====
# AWS RDS, Azure Database, 자체 MySQL 서버 등의 연결 정보
DB_HOST=your-mysql-host.com           # 예: mysql.example.com, RDS endpoint 등
DB_PORT=3306
DB_DATABASE=myapp
DB_USER=your-db-user
DB_PASSWORD=your-db-password

# 로컬 MySQL 사용 시 (docker-compose.yml에서 mysql 서비스 활성화 필요)
# DB_HOST=mysql                       # Docker 내부 네트워크 호스트명
# DB_PORT=3306
# DB_DATABASE=myapp
# DB_USER=user
# DB_PASSWORD=password
# DB_ROOT_PASSWORD=rootpassword

# ===== Directus =====
DIRECTUS_PORT=8055
DIRECTUS_KEY=replace-with-random-value-min-32-chars
DIRECTUS_SECRET=replace-with-random-secret-value
DIRECTUS_ADMIN_EMAIL=admin@example.com
DIRECTUS_ADMIN_PASSWORD=admin
DIRECTUS_PUBLIC_URL=http://localhost:8055
CORS_ORIGIN=*

# ===== Redis =====
REDIS_PORT=6379
CACHE_ENABLED=true

# ===== Backend API (Custom - 필요시) =====
BACKEND_PORT=8000
JWT_SECRET=your-jwt-secret-key-min-32-chars
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

# ===== Frontend =====
VITE_API_URL=http://localhost:8055

# ===== External Services (필요시) =====
# OpenAI
# OPENAI_API_KEY=sk-...

# AWS S3
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
# AWS_S3_BUCKET=
# AWS_REGION=ap-northeast-2

# GitHub Integration
# GITHUB_CLIENT_ID=
# GITHUB_CLIENT_SECRET=
# GITHUB_WEBHOOK_SECRET=

# Email (SMTP)
# SMTP_HOST=smtp.gmail.com
# SMTP_PORT=587
# SMTP_USER=
# SMTP_PASSWORD=
```

---

### .gitignore

**경로**: `.gitignore`

```
# Environment
.env
.env.local
.env.*.local

# Docker volumes
.docker/

# Dependencies
node_modules/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg
*.egg-info/
dist/
build/
.venv/
venv/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Build outputs
frontend/dist/
frontend/build/
mobile/.expo/
mobile/dist/

# Logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Testing
.coverage
htmlcov/
.pytest_cache/
.vitest/

# OS
Thumbs.db
.DS_Store

# Temporary
tmp/
temp/
*.tmp
```

---

## Backend (Python FastAPI)

### backend/Dockerfile

**경로**: `backend/Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### backend/requirements.txt

**경로**: `backend/requirements.txt`

```
# Web Framework
fastapi==0.109.0
uvicorn[standard]==0.27.0

# Database
sqlmodel==0.0.14
pymysql==1.1.0
cryptography==42.0.0

# Data Validation
pydantic==2.5.3
pydantic-settings==2.1.0

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# Cache
redis==5.0.1

# Async
celery==5.3.6

# Utilities
python-dotenv==1.0.0
```

---

### backend/src/main.py

**경로**: `backend/src/main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Project API",
    description="Custom Backend API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Import routers here
# from src.routes import example
# app.include_router(example.router)
```

---

### backend/src/models/__init__.py

**경로**: `backend/src/models/__init__.py`

```python
# SQLModel models here
```

---

### backend/src/routes/__init__.py

**경로**: `backend/src/routes/__init__.py`

```python
# API routes here
```

---

### backend/src/services/__init__.py

**경로**: `backend/src/services/__init__.py`

```python
# Business logic services here
```

---

## Frontend (React + Vite)

### frontend/package.json

**경로**: `frontend/package.json`

> ⚠️ **Tailwind CSS v4 주요 변경사항**: v4에서는 `postcss`, `autoprefixer`가 불필요하며, `@tailwindcss/postcss` 패키지를 사용합니다.

```json
{
  "name": "frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "type-check": "tsc --noEmit",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
  },
  "dependencies": {
    "@hookform/resolvers": "^5.2.2",
    "@tanstack/react-query": "^5.17.0",
    "lucide-react": "^0.563.0",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-hook-form": "^7.71.1",
    "react-router-dom": "^7.13.0",
    "zod": "^4.3.6",
    "zustand": "^5.0.10"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4.1.18",
    "@types/react": "^19.2.4",
    "@types/react-dom": "^19.2.4",
    "@vitejs/plugin-react": "^5.1.2",
    "eslint": "^9.28.0",
    "tailwindcss": "^4.1.18",
    "typescript": "~5.9.3",
    "vite": "^7.2.4"
  }
}
```

---

### frontend/.env.example

**경로**: `frontend/.env.example`

```bash
# API URL
VITE_API_URL=http://localhost:8055

# Production
# VITE_API_URL=https://api.yourdomain.com
```

**참고**: Frontend는 Dockerfile을 사용하지 않습니다.
- 개발: `pnpm dev`
- 운영: `pnpm build` 후 dist/를 Host Nginx/Apache로 서빙

---

### frontend/vite.config.ts

**경로**: `frontend/vite.config.ts`

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    host: true,
  },
})
```

---

### frontend/tsconfig.json

**경로**: `frontend/tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

---

### frontend/src/main.tsx

**경로**: `frontend/src/main.tsx`

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

---

### frontend/src/App.tsx

**경로**: `frontend/src/App.tsx`

```typescript
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="min-h-screen bg-gray-50">
        <h1 className="text-3xl font-bold text-center py-8">
          Project Frontend
        </h1>
      </div>
    </QueryClientProvider>
  )
}

export default App
```

---

### frontend/src/index.css

**경로**: `frontend/src/index.css`

> ⚠️ **Tailwind CSS v4 주요 변경사항**: `@tailwind` 지시어 대신 `@import 'tailwindcss'` 사용. 커스텀 테마는 `@theme` 블록에서 CSS 변수로 정의.

```css
@import 'tailwindcss';

@theme {
  /* 커스텀 테마 변수 (프로젝트에 맞게 수정) */
  /* --color-primary: #10b981; */
  /* --color-secondary: #3b82f6; */
}
```

---

### frontend/src/lib/api.ts

**경로**: `frontend/src/lib/api.ts`

```typescript
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8055'

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})
```

---

### frontend/index.html

**경로**: `frontend/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Project Frontend</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

---

## Mobile (Expo)

### mobile/package.json

**경로**: `mobile/package.json`

> ⚠️ **NativeWind v4 필수 의존성**: `nativewind`, `react-native-css-interop`, `react-native-reanimated` 모두 필요합니다.
> **참고**: NativeWind v4는 Tailwind CSS v3을 사용합니다 (v4 아님).

```json
{
  "name": "mobile",
  "version": "1.0.0",
  "main": "expo-router/entry",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "@tanstack/react-query": "^5.17.0",
    "expo": "~54.0.32",
    "expo-router": "^6.0.22",
    "nativewind": "^4.2.1",
    "react": "19.1.0",
    "react-native": "0.81.5",
    "react-native-css-interop": "^0.2.1",
    "react-native-reanimated": "~4.1.6",
    "react-native-safe-area-context": "5.4.0",
    "react-native-screens": "~4.11.1",
    "zustand": "^5.0.10"
  },
  "devDependencies": {
    "@babel/core": "^7.23.0",
    "@types/react": "~19.0.0",
    "tailwindcss": "^3.4.19",
    "typescript": "^5.3.3"
  }
}
```

---

### NativeWind v4 설정 파일들 (CRITICAL)

> ⚠️ **NativeWind v4 필수 설정 체크리스트:**
> 1. `babel.config.js` - jsxImportSource와 nativewind/babel 프리셋 필수
> 2. `metro.config.js` - withNativeWind 래퍼 필수
> 3. `tailwind.config.js` - nativewind/preset 프리셋 필수
> 4. `global.css` - @tailwind 지시어 포함
> 5. `app/_layout.tsx`에서 global.css import 필수
>
> 설정 누락 시 스타일이 적용되지 않으며, 에러 메시지 없이 실패할 수 있습니다.

---

### mobile/babel.config.js

**경로**: `mobile/babel.config.js`

> ⚠️ **CRITICAL**: NativeWind v4는 이 설정이 필수입니다. `jsxImportSource: 'nativewind'`와 `nativewind/babel` 프리셋이 없으면 스타일이 적용되지 않습니다.

```javascript
module.exports = function (api) {
  api.cache(true);
  return {
    presets: [
      ['babel-preset-expo', { jsxImportSource: 'nativewind' }],
      'nativewind/babel',
    ],
    plugins: ['react-native-reanimated/plugin'],
  };
};
```

---

### mobile/metro.config.js

**경로**: `mobile/metro.config.js`

```javascript
const { getDefaultConfig } = require('expo/metro-config');
const { withNativeWind } = require('nativewind/metro');

const config = getDefaultConfig(__dirname);

module.exports = withNativeWind(config, { input: './global.css' });
```

---

### mobile/tailwind.config.js

**경로**: `mobile/tailwind.config.js`

> **참고**: Mobile은 Tailwind CSS v3을 사용합니다 (NativeWind v4 호환).

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{js,jsx,ts,tsx}', './components/**/*.{js,jsx,ts,tsx}'],
  presets: [require('nativewind/preset')],
  theme: {
    extend: {
      colors: {
        // 커스텀 색상 (프로젝트에 맞게 수정)
        // primary: '#10b981',
        // secondary: '#3b82f6',
      },
    },
  },
  plugins: [],
};
```

---

### mobile/global.css

**경로**: `mobile/global.css`

> **참고**: NativeWind는 Tailwind CSS v3 문법을 사용합니다 (Frontend의 v4와 다름).

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

### mobile/app.json

**경로**: `mobile/app.json`

```json
{
  "expo": {
    "name": "mobile",
    "slug": "mobile",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "light",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#ffffff"
    },
    "assetBundlePatterns": [
      "**/*"
    ],
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.yourcompany.mobile"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#ffffff"
      },
      "package": "com.yourcompany.mobile"
    },
    "web": {
      "favicon": "./assets/favicon.png"
    },
    "scheme": "mobile"
  }
}
```

---

### mobile/tsconfig.json

**경路**: `mobile/tsconfig.json`

```json
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": {
    "strict": true
  }
}
```

---

### mobile/app/_layout.tsx

**경로**: `mobile/app/_layout.tsx`

> ⚠️ **CRITICAL**: `global.css` import가 필수입니다. 이 import가 없으면 NativeWind 스타일이 적용되지 않습니다.

```typescript
import '../global.css';
import { Stack } from 'expo-router';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

export default function RootLayout() {
  return (
    <QueryClientProvider client={queryClient}>
      <Stack>
        <Stack.Screen name="index" options={{ title: 'Home' }} />
      </Stack>
    </QueryClientProvider>
  );
}
```

---

### mobile/app/index.tsx

**경로**: `mobile/app/index.tsx`

```typescript
import { View, Text, StyleSheet } from 'react-native'

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Mobile App</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
})
```

---

### mobile/lib/api.ts

**경로**: `mobile/lib/api.ts`

```typescript
import axios from 'axios'

const API_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8055'

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add auth token to requests
api.interceptors.request.use(async (config) => {
  // const token = await AsyncStorage.getItem('auth_token')
  // if (token) {
  //   config.headers.Authorization = `Bearer ${token}`
  // }
  return config
})
```

---

## 디렉토리 구조

스킬이 생성할 전체 프로젝트 구조:

```
project-root/
├── IDEA.md                      # 프로젝트 아이디어 (시작점)
├── README.md                    # 프로젝트 소개
├── docker-compose.yml           # Docker 서비스 정의 (Backend만)
├── .env.example                # 환경 변수 예시
├── .gitignore                  # Git 무시 파일
├── .docker/                     # Docker 마운트 디렉토리
│   ├── directus/               # Directus 업로드/확장
│   │   ├── uploads/
│   │   └── extensions/
│   └── redis/                  # Redis 데이터
├── docs/                        # 프로젝트 문서
│   ├── 01-PRD.md
│   ├── 02-ARCHITECTURE.md
│   ├── 03-API_SPEC.md
│   ├── 04-DATABASE_SCHEMA.md
│   ├── 05-DEVELOPMENT_GUIDE.md
│   ├── 06-DEPLOYMENT.md
│   └── 07-MVP_CHECKLIST.md
├── backend/                     # Custom Backend (선택)
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── src/
│       ├── main.py
│       ├── config.py
│       ├── models/
│       │   └── __init__.py
│       ├── routes/
│       │   └── __init__.py
│       └── services/
│           └── __init__.py
├── frontend/                    # React Frontend (정적 배포)
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── index.html
│   ├── .env.example
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── pages/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   │   └── api.ts
│   │   └── types/
│   ├── public/
│   └── dist/                   # 빌드 후 생성 (pnpm build)
└── mobile/                      # Expo Mobile + NativeWind v4
    ├── package.json
    ├── app.json
    ├── tsconfig.json
    ├── babel.config.js          # NativeWind v4 필수
    ├── metro.config.js          # NativeWind v4 필수
    ├── tailwind.config.js       # NativeWind v4 필수
    ├── global.css               # NativeWind v4 필수
    ├── app/
    │   ├── _layout.tsx          # global.css import 필수
    │   ├── index.tsx
    │   └── (tabs)/
    ├── components/
    ├── lib/
    │   └── api.ts
    └── assets/
```

**주요 차이점**:
- Frontend: Dockerfile 없음, pnpm build로 dist/ 생성
- 배포: dist/를 Host Nginx/Apache로 서빙
- docker-compose.yml: Backend 서비스만 포함

---

## 사용 가이드

### 1. 기본 프로젝트 생성 (Directus만)

```bash
# 스킬이 생성할 파일들:
- docker-compose.yml (directus + redis만 활성화, frontend 제외)
- .env.example
- .gitignore
- frontend/ (Dockerfile 없음, pnpm build로 배포)
- mobile/
- docs/
```

**Frontend 배포**:
```bash
cd frontend
pnpm install
pnpm build
# dist/ 디렉토리를 Host 웹서버로 배포
```

### 2. 커스텀 백엔드 포함 프로젝트

```bash
# IDEA.md에 AI 기능, 복잡한 비즈니스 로직 명시 시:
- backend/ 디렉토리 추가 생성
- docker-compose.yml에서 backend 서비스 활성화
```

### 3. Frontend 배포

```bash
# 개발 환경
cd frontend
pnpm install
pnpm dev           # http://localhost:5173

# 운영 환경 빌드
pnpm build         # dist/ 생성

# Nginx 배포 예시
sudo cp -r dist/* /var/www/html/
# 또는
sudo rsync -avz dist/ /usr/share/nginx/html/
```

### 3. 로컬 MySQL 포함

```bash
# 외부 MySQL 접근이 어려운 경우:
- docker-compose.yml에서 mysql 서비스 주석 해제
- .env에서 DB_HOST=mysql로 설정
```

---

**템플릿 버전**: 3.0 (React 19, Tailwind v4, Expo 54, NativeWind v4)
**업데이트**: 2026-01-29

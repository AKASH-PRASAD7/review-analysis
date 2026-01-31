# Customer Review Analysis Platform

For analyzing customer reviews using AI-powered topic classification. Built with modern architecture patterns and industry best practices.

[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [Development](#-development)

---

## 🎯 Overview

A sophisticated full-stack application that analyzes customer reviews by breaking them into sentences and classifying each by topic (Performance, Billing, Support, UX, Account, Other). The system uses a hybrid approach combining keyword matching and LLM-based classification for accurate results.

**Key Capabilities:**
- 🤖 AI-powered sentence classification using Google FLAN-T5
- 🎨 Modern, responsive UI with real-time analysis
- 🏗️ Clean architecture with separation of concerns
- 🔒 Type-safe throughout (TypeScript + Python type hints)
- 📊 Production-ready error handling and logging
- 🚀 Optimized for scalability and maintainability

---

## ✨ Features

### Frontend
- ✅ **TypeScript** with strict mode for complete type safety
- ✅ **TanStack Query** for server state management with caching
- ✅ **Feature-based architecture** for scalability
- ✅ **Reusable component library** (Button, Loader, Card, etc.)
- ✅ **Custom hooks** for business logic separation
- ✅ **Path aliases** (`@/`) for clean imports
- ✅ **Responsive design** with modern CSS
- ✅ **Visual Analytics** with Topic Legend and Summary
- ✅ **Advanced Caching** with TanStack Query (debounced input, stale time)
- ✅ **Color-coded topic badges** for instant visual feedback

### Backend
- ✅ **Clean Architecture** (API → Services → Models)
- ✅ **Pydantic V2** for validation and serialization
- ✅ **Dependency Injection** for testability
- ✅ **Versioned API** (`/api/v1/`) for backward compatibility
- ✅ **Global error handling** with structured logging
- ✅ **Configuration management** with environment variables
- ✅ **Database-ready design** (no DB currently, but prepared)
- ✅ **OpenAPI documentation** auto-generated
- ✅ **In-memory Caching** for optimized repeated analysis

---

## 🏛️ Architecture

### Frontend Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     React Application                    │
├─────────────────────────────────────────────────────────┤
│  Components (Presentational)                             │
│  ├─ Common: Button, Loader, ErrorMessage, EmptyState   │
│  └─ Layout: Card, Container                             │
├─────────────────────────────────────────────────────────┤
│  Features (Business Logic)                               │
│  └─ review-analysis/                                     │
│     ├─ components/ (Container components)               │
│     ├─ hooks/ (useReviewAnalysis)                       │
│     └─ types/ (Feature-specific types)                  │
├─────────────────────────────────────────────────────────┤
│  API Layer                                               │
│  ├─ client.ts (Axios instance)                          │
│  ├─ queries.ts (TanStack Query hooks)                   │
│  └─ types.ts (API response types)                       │
└─────────────────────────────────────────────────────────┘
```

### Backend Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Application                   │
├─────────────────────────────────────────────────────────┤
│  API Layer (app/api/v1/)                                │
│  ├─ routers/analyze.py (POST /api/v1/analyze)          │
│  ├─ routers/health.py (GET /api/v1/health)             │
│  └─ dependencies.py (Dependency injection)              │
├─────────────────────────────────────────────────────────┤
│  Service Layer (app/services/)                          │
│  ├─ ReviewAnalysisService (Orchestration)              │
│  └─ LLMService (Model inference)                        │
├─────────────────────────────────────────────────────────┤
│  Domain Layer (app/models/)                             │
│  ├─ Sentence (Domain entity)                            │
│  └─ Topic (Enum with validation)                        │
├─────────────────────────────────────────────────────────┤
│  Schema Layer (app/schemas/)                            │
│  ├─ AnalyzeRequest/Response (Pydantic models)          │
│  └─ HealthResponse (Health check schema)               │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
| Technology | Purpose | Version |
|------------|---------|---------|
| **React** | UI Framework | 19.x |
| **TypeScript** | Type Safety | 5.x |
| **Vite** | Build Tool | 6.x |
| **TanStack Query** | Server State | 5.x |
| **Axios** | HTTP Client | 1.x |

### Backend
| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | Web Framework | Latest |
| **Python** | Language | 3.10+ |
| **Pydantic** | Validation | 2.x |
| **Transformers** | LLM Library | Latest |
| **PyTorch** | ML Framework | Latest |

### AI Model
- **Model**: Google FLAN-T5-Small
- **Size**: ~250MB
- **Approach**: Hybrid (Keywords + LLM)
- **Inference**: CPU-based with few-shot prompting

---

## 📁 Project Structure

```
review-analysis/
├── frontend/                      # React + TypeScript frontend
│   ├── src/
│   │   ├── api/                  # API layer
│   │   │   ├── client.ts         # Axios instance
│   │   │   ├── endpoints.ts      # API routes
│   │   │   ├── queryKeys.ts      # Query key factory
│   │   │   ├── queries.ts        # TanStack Query hooks
│   │   │   └── types.ts          # API types
│   │   │
│   │   ├── components/
│   │   │   ├── common/           # Reusable UI components
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Loader.tsx
│   │   │   │   ├── ErrorMessage.tsx
│   │   │   │   └── EmptyState.tsx
│   │   │   └── layout/           # Layout components
│   │   │       ├── Card.tsx
│   │   │       └── Container.tsx
│   │   │
│   │   ├── features/
│   │   │   └── review-analysis/  # Feature module
│   │   │       ├── components/   # Feature components
│   │   │       ├── hooks/        # Custom hooks
│   │   │       └── types.ts      # Feature types
│   │   │
│   │   ├── utils/                # Utilities
│   │   ├── App.tsx               # Main app
│   │   └── main.tsx              # Entry point
│   │
│   ├── tsconfig.json             # TypeScript config
│   ├── vite.config.ts            # Vite config
│   └── package.json
│
├── backend/                       # FastAPI backend
│   ├── app/
│   │   ├── core/                 # Core infrastructure
│   │   │   ├── config.py         # Settings (Pydantic)
│   │   │   ├── logging.py        # Logging setup
│   │   │   └── exceptions.py     # Custom exceptions
│   │   │
│   │   ├── api/
│   │   │   └── v1/               # API version 1
│   │   │       ├── routers/
│   │   │       │   ├── analyze.py
│   │   │       │   └── health.py
│   │   │       ├── dependencies.py
│   │   │       └── api_router.py
│   │   │
│   │   ├── schemas/              # Pydantic schemas
│   │   │   ├── analyze.py
│   │   │   └── health.py
│   │   │
│   │   ├── services/             # Business logic
│   │   │   ├── llm_service.py
│   │   │   └── review_analysis_service.py
│   │   │
│   │   ├── models/               # Domain models
│   │   │   ├── sentence.py
│   │   │   └── topic.py
│   │   │
│   │   ├── utils/                # Utilities
│   │   │   └── text_processing.py
│   │   │
│   │   └── main.py               # FastAPI app
│   │
│   ├── .env.example              # Environment template
│   ├── requirements.txt          # Python dependencies
│   └── Procfile                  # Deployment config
│
└── README.md                      # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.10+
- **pip** package manager

### Installation

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd review-analysis
```

#### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (optional)
cp .env.example .env

# Start the server
uvicorn app.main:app --reload
```

**Backend runs at**: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/api/v1/health`

#### 3. Frontend Setup

```bash
# Navigate to frontend (from root)
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

**Frontend runs at**: `http://localhost:5173`

273: **Frontend runs at**: `http://localhost:5173`

---

## 🧪 Testing

### Backend Tests
The backend includes unit tests for API endpoints and caching logic.

```bash
# Activate virtual environment
source venv/bin/activate

# Run tests with pytest
pytest backend/tests/test_api.py -v
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api/v1
```

### Endpoints

#### 1. Health Check
```http
GET /api/v1/health
```

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true,
  "model_name": "google/flan-t5-small"
}
```

#### 2. Analyze Review
```http
POST /api/v1/analyze
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "The app crashes frequently. Customer support was helpful. The billing is confusing."
}
```

**Response:**
```json
{
  "sentences": [
    {
      "index": 0,
      "text": "The app crashes frequently.",
      "topic": "Performance"
    },
    {
      "index": 1,
      "text": "Customer support was helpful.",
      "topic": "Support"
    },
    {
      "index": 2,
      "text": "The billing is confusing.",
      "topic": "Billing"
    }
  ]
}
```

### Topic Categories
- **Performance**: App speed, crashes, lag
- **Billing**: Charges, refunds, pricing
- **Support**: Customer service, help
- **UX**: User interface, design
- **Account**: Login, authentication
- **Other**: Uncategorized

### Interactive Documentation
Visit `http://localhost:8000/docs` for Swagger UI with:
- Interactive API testing
- Request/response schemas
- Authentication (if added)
- Example requests

---


## 💻 Development

### Frontend Development

#### Build for Production
```bash
npm run build
```

#### Preview Production Build
```bash
npm run preview
```

### Backend Development

#### Run with Auto-reload
```bash
uvicorn app.main:app --reload --log-level debug
```

#### Type Checking (with mypy)
```bash
mypy app/
```

#### Linting (with ruff)
```bash
ruff check app/
```

#### Format Code
```bash
black app/
```

### Adding New Features

#### Frontend: New Feature Module
1. Create `src/features/feature-name/`
2. Add `components/`, `hooks/`, `types.ts`
3. Export from `index.ts`
4. Import in `App.tsx`

#### Backend: New Endpoint
1. Create router in `app/api/v1/routers/`
2. Define schemas in `app/schemas/`
3. Implement service in `app/services/`
4. Register in `app/api/v1/api_router.py`

---

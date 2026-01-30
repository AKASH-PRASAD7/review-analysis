# LLM-Powered Customer Review Topic Highlighter

A simple, modern web application that analyzes customer reviews using a local generative LLM and highlights sentences by topic.

## 🚀 Live Demo

- **Frontend**: [Deploy to Netlify](https://app.netlify.com/start/deploy?repository=...) (Replace with actual link)
- **Backend**: [Deploy to Render](https://render.com) (Replace with actual link)

## 🏗 Stack

- **Frontend**: React (Vite)
- **Backend**: Python (FastAPI)
- **AI**: TinyLlama-1.1B (GGUF) via `llama-cpp-python`

## 🏃 Run Globally

### Backend

1. Navigate to `backend`:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: `llama-cpp-python` may require a C++ compiler. See [installation guide](https://github.com/abetlen/llama-cpp-python) if issues arise.*

3. Download the Model:
   ```bash
   python scripts/download_model.py
   ```
   This downloads `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` (~670MB) to `backend/models/`.

4. Start the Server:
   ```bash
   uvicorn main:app --reload
   ```
   Server runs at `http://localhost:8000`.

### Frontend

1. Navigate to `frontend`:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start Dev Server:
   ```bash
   npm run dev
   ```
   App runs at `http://localhost:5173`.

## 📦 Deployment Instructions

### Backend (Render/Railway)

1. Push this repo to GitHub.
2. Create a new **Web Service**.
3. Set **Root Directory** to `backend`.
4. Set **Build Command** to:
   ```bash
   pip install -r requirements.txt && python scripts/download_model.py
   ```
5. Set **Start Command** to:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Ensure the instance has at least 1GB RAM (Free tier usually has 512MB - might be tight for 1.1B model. Quantized 0.5B (Qwen) is an alternative if OOM occurs).

### Frontend (Netlify/Vercel)

1. Create a new site from Git.
2. Set **Base Directory** to `frontend`.
3. Set **Build Command** to `npm run build`.
4. Set **Publish Directory** to `dist`.
5. Add Environment Variable:
   - `VITE_API_URL`: The URL of your deployed backend (e.g. `https://my-api.onrender.com`).

## 🧠 Design Decisions

- **Modular**: Backend and Frontend are separated.
- **Robust**: Strict JSON parsing with fallback to "Other" topic.
- **Efficient**: Uses `llama-cpp-python` for fast CPU inference.
- **Aesthetic**: Custom dark mode UI with glassmorphism effects.

## 🔮 Future Improvements

- [ ] Add Topic Legend (Visual key).
- [ ] Implement Caching (Redis) for repeated queries.
- [ ] Add Unit Tests for Frontend components.

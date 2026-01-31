from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from utils.text_processing import split_into_sentences
from core.llm import llm_service

app = FastAPI(title="Customer Review Topic Highlighter")

# CORS - Allow all for demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str

class SentenceResult(BaseModel):
    index: int
    text: str
    topic: str

class AnalyzeResponse(BaseModel):
    sentences: List[SentenceResult]

@app.on_event("startup")
async def startup_event():
    print("Starting up... Loading LLM model")
    llm_service.load_model()

# Simple in-memory cache
analysis_cache = {}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_review(request: AnalyzeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")

    # Check cache
    if request.text in analysis_cache:
        print("Cache hit!")
        return analysis_cache[request.text]

    # 1. Split sentences
    sentences = split_into_sentences(request.text)

    # 2. Analyze each sentence
    results = []
    for idx, sentence in enumerate(sentences):
        topic = llm_service.analyze_sentence(sentence)
        results.append(SentenceResult(
            index=idx,
            text=sentence,
            topic=topic
        ))

    response = AnalyzeResponse(sentences=results)
    
    # Store in cache
    analysis_cache[request.text] = response
    
    return response

@app.get("/health")
def health_check():
    return {"status": "ok"}

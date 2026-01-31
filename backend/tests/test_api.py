from fastapi.testclient import TestClient
import sys
import os

# Add backend to path so we can import app
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_review():
    response = client.post("/analyze", json={"text": "The app is fast."})
    assert response.status_code == 200
    data = response.json()
    assert "sentences" in data
    assert len(data["sentences"]) > 0
    assert data["sentences"][0]["text"] == "The app is fast."

def test_analyze_empty_review():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 400

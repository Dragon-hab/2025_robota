from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_events_returns_list():
    r = client.get("/api/events")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_event_invalid_payload():
    # Некоректні дані: порожній title (або відсутній)
    payload = {
        "title": "",
        "description": "test",
        "start_at": "2025-10-10T10:00:00",
        "location": "Kyiv"
    }
    r = client.post("/api/events", json=payload)
    # FastAPI/Pydantic зазвичай повертає 422
    assert r.status_code in (400, 422)

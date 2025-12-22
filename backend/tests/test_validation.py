from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event_missing_required_fields():
    # Відсутні обов'язкові поля
    r = client.post("/api/events", json={})
    assert r.status_code in (400, 422)

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_docs_available():
    # Swagger сторінка має існувати (швидка перевірка що app стартує)
    r = client.get("/docs")
    assert r.status_code == 200

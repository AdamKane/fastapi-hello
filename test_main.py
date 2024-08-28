from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_say_hello():
    response = client.get("/hello/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Alice"}

def test_count_leads():
    response = client.get("/leads/count")
    assert response.status_code == 200
    assert "total_leads" in response.json()
    assert isinstance(response.json()["total_leads"], int)
    assert response.json()["total_leads"] >= 0


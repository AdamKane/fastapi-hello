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

def test_say_hello_empty_name():
    response = client.get("/hello/")
    assert response.status_code == 404

def test_say_hello_special_characters():
    response = client.get("/hello/John%20Doe")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John Doe"}

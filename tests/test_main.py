import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI Service Running"}

def test_create_item():
    response = client.post("/items", json={"name": "Test", "price": 10.5})
    assert response.status_code == 201
    assert response.json()["name"] == "Test"

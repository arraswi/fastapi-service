import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_and_get_item():
    response = client.post("/items", json={"name": "Test Item", "price": 10.5})
    assert response.status_code == 201
    item = response.json()
    assert item["name"] == "Test Item"
    
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_update_item():
    client.post("/items", json={"name": "Item1", "price": 10.0})
    response = client.put("/items/1", json={"name": "Updated", "price": 20.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"

def test_delete_item():
    client.post("/items", json={"name": "ToDelete", "price": 5.0})
    response = client.delete("/items/1")
    assert response.status_code == 200

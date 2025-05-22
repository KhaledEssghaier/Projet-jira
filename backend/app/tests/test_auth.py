import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Register a new user
    response = client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpass123",
        "is_student": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "testuser@example.com"

    # Login with the new user
    response = client.post("/auth/login", data={
        "username": "testuser@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token

    # Access protected route
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

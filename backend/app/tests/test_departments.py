import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_department():
    # Register and login
    client.post("/auth/register", json={
        "email": "deptadmin@example.com",
        "password": "adminpass",
        "is_student": False,
        "role": "admin"
    })
    login = client.post("/auth/login", data={
        "username": "deptadmin@example.com",
        "password": "adminpass"
    })
    token = login.json()["access_token"]
    # Create department
    response = client.post("/departments/", json={"name": "Informatique"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["name"] == "Informatique"

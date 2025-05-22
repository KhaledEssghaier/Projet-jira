import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_enroll_formation():
    # Register and login
    client.post("/auth/register", json={
        "email": "student1@example.com",
        "password": "studpass",
        "is_student": True
    })
    login = client.post("/auth/login", data={
        "username": "student1@example.com",
        "password": "studpass"
    })
    token = login.json()["access_token"]
    # Create formation
    response = client.post("/formations/", json={"theme": "Python", "description": "Cours Python"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    formation_id = response.json()["id"]
    # Enroll student
    user = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"}).json()
    enroll = client.post("/enrollments/", json={"student_id": user["id"], "formation_id": formation_id}, headers={"Authorization": f"Bearer {token}"})
    assert enroll.status_code == 200
    assert enroll.json()["student_id"] == user["id"]
    assert enroll.json()["formation_id"] == formation_id

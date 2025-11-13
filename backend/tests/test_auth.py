from conftest import client as c

client = c


def test_register(client):
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "test12345",
    }

    response = client.post("/api/v1/auth/register", json=data)

    assert response.status_code == 201
    body = response.json()

    assert "id" in body
    assert body["username"] == "testuser"
    assert body["email"] == "test@example.com"


def test_login(client):
    data = {"username": "testuser", "password": "test12345"}

    response = client.post("/api/v1/auth/login", json=data)

    assert response.status_code == 200
    body = response.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"

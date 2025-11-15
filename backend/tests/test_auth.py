from conftest import client as c

client = c


def test_register(client):
    data = {
        "username": "testuserq",
        "email": "testq@example.com",
        "password": "testq12345",
    }

    response = client.post("/api/v1/auth/register", json=data)

    assert response.status_code == 201
    body = response.json()

    assert "id" in body
    assert body["username"] == "testuserq"
    assert body["email"] == "testq@example.com"

    # First registered user is always admin by design
    assert body["role"] in ["admin", "user"]


def test_login(client):
    # First register
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuserw",
            "email": "testw@example.com",
            "password": "test12345",
        },
    )

    # Then login
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "testuserw", "password": "test12345"},
    )

    assert response.status_code == 200
    body = response.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"

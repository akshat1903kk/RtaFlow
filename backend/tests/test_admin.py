# from app.database import Base, engine
from conftest import client as c

client = c


# def create_admin_and_login(client):
#     # Create admin user (first user in fresh DB)
#     reg_data = {
#         "username": "adminuser",
#         "email": "admin@example.com",
#         "password": "strongpass123",
#     }
#     client.post("/api/v1/auth/register", json=reg_data)

#     # Login
#     login_data = {"username": "adminuser", "password": "strongpass123"}
#     res = client.post("/api/v1/auth/login", json=login_data)
#     token = res.json()["access_token"]

#     return {"Authorization": f"Bearer {token}"}


def test_fetch_all(client):
    # The 'client' fixture already has the admin token in its headers
    response = client.get("/api/v1/admin/dashboard/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_fetch_one(client):
    # The 'client' fixture's user ("testuser") is the admin and has ID 1
    response = client.get("/api/v1/admin/dashboard/users/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["role"] == "admin"
    # This should be "testuser" as defined in conftest.py
    assert body["username"] == "testuser"

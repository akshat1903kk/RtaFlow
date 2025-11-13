from conftest import client as c

client = c


def test_health(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

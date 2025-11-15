def test_create_entry(client):
    data = {"title": "My Entry", "content": "Deep thoughts"}
    response = client.post("/api/v1/journal/", json=data)
    assert response.status_code == 201

    body = response.json()
    assert body["title"] == "My Entry"
    assert body["content"] == "Deep thoughts"


def test_get_all_entries(client):
    response = client.get("/api/v1/journal/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_entry(client):
    new = client.post(
        "/api/v1/journal/", json={"title": "abc", "content": "xyz"}
    ).json()
    entry_id = new["id"]

    response = client.get(f"/api/v1/journal/{entry_id}")
    assert response.status_code == 200
    assert response.json()["id"] == entry_id


def test_update_entry(client):
    new = client.post(
        "/api/v1/journal/", json={"title": "old", "content": "old"}
    ).json()
    entry_id = new["id"]

    response = client.put(
        f"/api/v1/journal/{entry_id}", json={"title": "updated title"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


def test_delete_entry(client):
    new = client.post("/api/v1/journal/", json={"title": "del", "content": "me"}).json()
    entry_id = new["id"]

    response = client.delete(f"/api/v1/journal/{entry_id}")
    assert response.status_code == 204

    # verify deletion
    response = client.get(f"/api/v1/journal/{entry_id}")
    assert response.status_code == 404

def test_create_task(client):
    data = {"title": "Test Task", "description": "Something important"}
    response = client.post("/api/v1/tasks/", json=data)
    assert response.status_code == 201

    body = response.json()
    assert body["title"] == "Test Task"
    assert body["description"] == "Something important"


def test_get_all_tasks(client):
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_one_task(client):
    # First create one
    new = client.post(
        "/api/v1/tasks/", json={"title": "abc", "description": "xyz"}
    ).json()
    task_id = new["id"]

    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task(client):
    new = client.post(
        "/api/v1/tasks/", json={"title": "old", "description": "old"}
    ).json()
    task_id = new["id"]

    response = client.put(f"/api/v1/tasks/{task_id}", json={"title": "new title"})
    assert response.status_code == 200
    assert response.json()["title"] == "new title"


def test_delete_task(client):
    new = client.post(
        "/api/v1/tasks/", json={"title": "delete", "description": "me"}
    ).json()
    task_id = new["id"]

    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 204

    # verify deletion
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 404

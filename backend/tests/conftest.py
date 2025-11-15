import pytest
from app.database import Base, engine, get_db
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

TEST_DB_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    with TestClient(app) as client:
        # create initial user
        register = client.post(
            "/api/v1/auth/register",
            json={
                "username": "testuser",
                "email": "test@example.com",
                "password": "testing123",
            },
        )

        # login user
        login = client.post(
            "/api/v1/auth/login",
            json={"username": "testuser", "password": "testing123"},
        )

        token = login.json()["access_token"]

        # ATTACH TOKEN TO CLIENT
        client.headers.update({"Authorization": f"Bearer {token}"})

        yield client

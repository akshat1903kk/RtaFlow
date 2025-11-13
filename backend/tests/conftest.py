# backend/tests/conftest.py
import pytest
from app.main import app  # ← correct import
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client():
    # This triggers FastAPI startup and shutdown events.
    with TestClient(app) as c:
        yield c

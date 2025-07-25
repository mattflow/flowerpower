from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_redirect_to_docs(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)
    assert response.status_code == HTTPStatus.TEMPORARY_REDIRECT
    assert response.headers["location"] == "/docs"


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": "ok"}

def test_greeting(client: TestClient) -> None:
    response = client.get("/greeting")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"greeting": "Hello world"}

    response = client.get("/greeting", params={"name": "test"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"greeting": "Hello test"}
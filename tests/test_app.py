
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"CI/CD Demo Application" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert b"healthy" in response.data


def test_version():
    client = app.test_client()
    response = client.get("/version")

    assert response.status_code == 200
    assert b"1.0" in response.data

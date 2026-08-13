import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def auth_token():
    response = requests.post(
        f"{BASE_URL}/api/login",
        json={
            "username": "admin",
            "password": "admin",
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


@pytest.fixture
def api_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}",
    }


@pytest.fixture
def reset_employees(api_headers):
    requests.post(
        f"{BASE_URL}/api/employees/reset",
        headers=api_headers,
    )

    yield

    requests.post(
        f"{BASE_URL}/api/employees/reset",
        headers=api_headers,
    )
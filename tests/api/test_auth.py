import requests

BASE_URL = "http://127.0.0.1:8000"


def test_login_returns_access_token(auth_token):
    assert auth_token


def test_login_with_invalid_credentials_returns_401():
    response = requests.post(
        f"{BASE_URL}/api/login",
        json={
            "username": "wrong",
            "password": "wrong",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"
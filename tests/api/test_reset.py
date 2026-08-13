import requests


BASE_URL = "http://127.0.0.1:8000"


def test_reset_employees_clears_all_employees(api_headers, reset_employees):
    employee = {
        "name": "Reset User",
        "salary": 30000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": False,
    }

    create_response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert create_response.status_code == 200

    reset_response = requests.post(
        f"{BASE_URL}/api/employees/reset",
        headers=api_headers,
    )

    assert reset_response.status_code == 200
    assert reset_response.json()["status"] == "reset"

    employees_response = requests.get(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
    )

    assert employees_response.status_code == 200
    assert employees_response.json() == []
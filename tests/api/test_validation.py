import requests


BASE_URL = "http://127.0.0.1:8000"


def test_create_employee_with_age_below_minimum_returns_422(
    api_headers, reset_employees
):
    employee = {
        "name": "Invalid Age",
        "salary": 30000,
        "age": 17,
        "position": "Junior QA",
        "on_leave": False,
    }

    response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 422


def test_create_employee_with_age_above_maximum_returns_422(
    api_headers, reset_employees
):
    employee = {
        "name": "Invalid Age",
        "salary": 30000,
        "age": 66,
        "position": "Junior QA",
        "on_leave": False,
    }

    response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 422


def test_create_employee_with_salary_below_minimum_returns_422(
    api_headers, reset_employees
):
    employee = {
        "name": "Invalid Salary",
        "salary": 0,
        "age": 30,
        "position": "Junior QA",
        "on_leave": False,
    }

    response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 422


def test_create_employee_with_invalid_position_returns_422(
    api_headers, reset_employees
):
    employee = {
        "name": "Invalid Position",
        "salary": 30000,
        "age": 30,
        "position": "CEO",
        "on_leave": False,
    }

    response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 422
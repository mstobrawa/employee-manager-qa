import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_employees_returns_list(api_headers, reset_employees):
    response = requests.get(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_employee_returns_created_employee(api_headers, reset_employees):
    employee = {
        "name": "Anna Kowalska",
        "salary": 40000,
        "age": 32,
        "position": "Mid QA",
        "on_leave": False,
    }

    response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Anna Kowalska"
    assert data["salary"] == 40000
    assert data["age"] == 32
    assert data["position"] == "Mid QA"
    assert data["on_leave"] is False


def test_update_employee_returns_updated_employee(api_headers, reset_employees):
    employee = {
        "name": "Anna Kowalska",
        "salary": 40000,
        "age": 32,
        "position": "Mid QA",
        "on_leave": False,
    }

    create_response = requests.post(
        f"{BASE_URL}/api/employees",
        headers=api_headers,
        json=employee,
    )

    employee_id = create_response.json()["id"]

    updated_employee = {
        "name": "Anna Updated",
        "salary": 50000,
        "age": 35,
        "position": "Senior QA",
        "on_leave": True,
    }

    response = requests.put(
        f"{BASE_URL}/api/employees/{employee_id}",
        headers=api_headers,
        json=updated_employee,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["name"] == "Anna Updated"
    assert data["salary"] == 50000
    assert data["age"] == 35
    assert data["position"] == "Senior QA"
    assert data["on_leave"] is True


def test_delete_employee_returns_deleted_status(api_headers, reset_employees):
    employee = {
        "name": "Delete User",
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

    employee_id = create_response.json()["id"]

    response = requests.delete(
        f"{BASE_URL}/api/employees/{employee_id}",
        headers=api_headers,
    )

    assert response.status_code == 200
    assert response.json()["status"] == "deleted"


def test_update_nonexistent_employee_returns_404(api_headers, reset_employees):
    employee = {
        "name": "Missing User",
        "salary": 30000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": False,
    }

    response = requests.put(
        f"{BASE_URL}/api/employees/999999",
        headers=api_headers,
        json=employee,
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_delete_nonexistent_employee_returns_404(api_headers, reset_employees):
    response = requests.delete(
        f"{BASE_URL}/api/employees/999999",
        headers=api_headers,
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"
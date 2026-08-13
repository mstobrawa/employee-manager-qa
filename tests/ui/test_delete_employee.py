from uuid import uuid4

from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_delete_employee(driver):
    employee_name = f"DeleteUser{uuid4().hex[:8]}"

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "admin")

    employee_page = EmployeePage(driver)
    employee_page.wait_for_page()

    employee_page.enter_employee_data(
        name=employee_name,
        salary=30000,
        age=30,
        position="Junior QA",
        on_leave=False,
    )

    employee_page.submit_employee()
    employee_page.wait_for_employee(employee_name)

    assert employee_name in employee_page.get_employee_names()

    employee_page.click_delete_for_employee(employee_name)

    employee_page.wait_for_employee_to_disappear(employee_name)

    assert employee_name not in employee_page.get_employee_names()

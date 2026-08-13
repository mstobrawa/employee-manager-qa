from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_edit_employee(driver):
    employee_name = f"EditUser{uuid4().hex[:8]}"
    updated_name = f"UpdatedUser{uuid4().hex[:8]}"

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "admin")

    employee_page = EmployeePage(driver)
    employee_page.wait_for_page()

    employee_page.enter_employee_data(
        name=employee_name,
        salary=40000,
        age=32,
        position="Mid QA",
        on_leave=False,
    )

    employee_page.submit_employee()
    employee_page.wait_for_employee(employee_name)

    employee_page.click_edit_for_employee(employee_name)

    assert employee_page.get_form_title() == "Edit Employee"

    employee_page.enter_employee_data(
        name=updated_name,
        salary=50000,
        age=35,
        position="Senior QA",
        on_leave=True,
    )

    employee_page.submit_employee()
    employee_page.wait_for_employee(updated_name)

    assert updated_name in employee_page.get_employee_names()
from uuid import uuid4

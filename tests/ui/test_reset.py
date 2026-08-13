from uuid import uuid4

from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_reset_modal_can_be_cancelled_and_confirmed(driver):
    employee_name = f"ResetUser{uuid4().hex[:8]}"

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
    )
    employee_page.submit_employee()
    employee_page.wait_for_employee(employee_name)

    employee_page.open_reset_modal()
    assert employee_page.is_reset_modal_visible()

    employee_page.cancel_reset()
    employee_page.wait_for_reset_modal_to_close()
    assert employee_name in employee_page.get_employee_names()

    employee_page.open_reset_modal()
    employee_page.confirm_reset()
    employee_page.wait_for_employee_to_disappear(employee_name)

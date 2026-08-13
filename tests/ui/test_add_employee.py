from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_add_employee(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "admin")

    employee_page = EmployeePage(driver)
    employee_page.wait_for_page()

    employee_page.enter_employee_data(
        name="Anna Kowalska",
        salary=40000,
        age=32,
        position="Mid QA",
        on_leave=False,
    )

    employee_page.submit_employee()
    employee_page.wait_for_employee("Anna Kowalska")

    assert "Anna Kowalska" in employee_page.get_employee_names()

from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_employee_age_validation_is_displayed(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "admin")

    employee_page = EmployeePage(driver)
    employee_page.wait_for_page()
    employee_page.enter_employee_data(
        name="Invalid Age",
        salary=30000,
        age=17,
        position="Junior QA",
    )

    employee_page.submit_employee()

    assert "age" in employee_page.get_error_message().lower()

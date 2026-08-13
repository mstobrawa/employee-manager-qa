from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_user_can_switch_between_dark_and_light_theme(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "admin")

    employee_page = EmployeePage(driver)
    employee_page.wait_for_page()

    employee_page.click_theme_toggle()
    employee_page.wait_for_theme("light")
    assert employee_page.get_body_class() == "light"

    employee_page.click_theme_toggle()
    employee_page.wait_for_theme("dark")
    assert employee_page.get_body_class() == "dark"

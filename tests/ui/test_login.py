from pages.login_page import LoginPage


def test_user_can_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("admin", "admin")

    assert "Employee Manager" in driver.title
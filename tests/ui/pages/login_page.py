from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "http://127.0.0.1:8000/"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_FORM = (By.ID, "loginForm")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_FORM)
        ).submit()
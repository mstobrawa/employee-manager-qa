from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class EmployeePage:
    URL = "http://127.0.0"

    NAME_INPUT = (By.ID, "name")
    SALARY_INPUT = (By.ID, "salary")
    AGE_INPUT = (By.ID, "age")
    POSITION_SELECT = (By.ID, "position")
    ON_LEAVE_CHECKBOX = (By.ID, "on_leave")

    SUBMIT_BUTTON = (By.ID, "submitBtn")
    FORM_TITLE = (By.ID, "form-title")
    ERROR_BOX = (By.ID, "errorBox")

    RESET_BUTTON = (By.CSS_SELECTOR, ".btn-reset")
    RESET_MODAL = (By.ID, "resetModal")
    RESET_CANCEL_BUTTON = (By.CSS_SELECTOR, "#resetModal .btn-cancel")
    RESET_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#resetModal .btn-confirm-danger")

    THEME_BUTTON = (
        By.CSS_SELECTOR,
        ".navbar-actions .toggle:not(.btn-reset)",
    )

    EMPLOYEE_ROWS = (By.CSS_SELECTOR, "#employees tr")
    EMPLOYEE_NAMES_LOCATOR = (By.CSS_SELECTOR, "#employees tr td:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

    def enter_employee_data(
        self,
        name,
        salary,
        age,
        position,
        on_leave=False,
    ):
        name_input = self.wait.until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )
        salary_input = self.wait.until(
            EC.visibility_of_element_located(self.SALARY_INPUT)
        )
        age_input = self.wait.until(
            EC.visibility_of_element_located(self.AGE_INPUT)
        )

        name_input.clear()
        name_input.send_keys(name)

        salary_input.clear()
        salary_input.send_keys(str(salary))

        age_input.clear()
        age_input.send_keys(str(age))

        select = Select(
            self.wait.until(
                EC.visibility_of_element_located(self.POSITION_SELECT)
            )
        )
        select.select_by_visible_text(position)

        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.ON_LEAVE_CHECKBOX)
        )

        if checkbox.is_selected() != on_leave:
            checkbox.click()

    def submit_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def employee_row(self, name):
        return (
            By.XPATH,
            f"//tbody[@id='employees']//tr[td[2][normalize-space()='{name}']]",
        )

    def wait_for_employee(self, name):
        self.wait.until(EC.presence_of_element_located(self.employee_row(name)))

    def wait_for_employee_to_disappear(self, name):
        self.wait.until(EC.invisibility_of_element_located(self.employee_row(name)))

    def get_form_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.FORM_TITLE)
        ).text

    def get_employee_names(self):
        names = self.driver.find_elements(*self.EMPLOYEE_NAMES_LOCATOR)
        return [name.text for name in names]

    def click_edit_for_employee(self, name):
        locator = (
            By.XPATH,
            f"//tbody[@id='employees']//tr[td[2][normalize-space()='{name}']]"
            "//button[contains(@class, 'btn-edit')]",
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_delete_for_employee(self, name):
        locator = (
            By.XPATH,
            f"//tbody[@id='employees']//tr[td[2][normalize-space()='{name}']]"
            "//button[contains(@class, 'btn-delete')]",
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_BOX)
        ).text

    def open_reset_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.RESET_BUTTON)
        ).click()

    def is_reset_modal_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RESET_MODAL)
        ).is_displayed()

    def cancel_reset(self):
        self.wait.until(
            EC.element_to_be_clickable(self.RESET_CANCEL_BUTTON)
        ).click()

    def wait_for_reset_modal_to_close(self):
        self.wait.until(EC.invisibility_of_element_located(self.RESET_MODAL))

    def confirm_reset(self):
        self.wait.until(
            EC.element_to_be_clickable(self.RESET_CONFIRM_BUTTON)
        ).click()

    def click_theme_toggle(self):
        self.wait.until(
            EC.element_to_be_clickable(self.THEME_BUTTON)
        ).click()

    def get_body_class(self):
        return self.driver.find_element(
            By.TAG_NAME, "body"
        ).get_attribute("class")

    def wait_for_theme(self, theme):
        self.wait.until(
            lambda driver: driver.find_element(By.TAG_NAME, "body").get_attribute("class")
            == theme
        )

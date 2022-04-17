from selenium.webdriver.common.by import By
from src.base_page import BasePage
import allure


class RegisterAccountLocators:
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    AGREE_PRIVACY_POLICY = (By.XPATH, "//input[@type='checkbox']")
    CONTINUE_BTN = (By.XPATH, "//input[@value='Continue']")


class RegisterAccount(BasePage):
    def check_input_first_name(self):
        with allure.step("Проверка поля ввода first name"):
            self.find_element(RegisterAccountLocators.FIRST_NAME)
            return True

    def check_input_last_name(self):
        with allure.step("Проверка поля ввода last name"):
            self.find_element(RegisterAccountLocators.LAST_NAME)
            return True

    def check_email(self):
        with allure.step("Проверка поля ввода first email"):
            self.find_element(RegisterAccountLocators.EMAIL)
            return True

    def send_first_name(self, firstname):
        with allure.step("Ввод в поле first name"):
            self.find_element(RegisterAccountLocators.FIRST_NAME).send_keys(firstname)

    def send_last_name(self, lastname):
        with allure.step("Проверка поля ввода last name"):
            self.find_element(RegisterAccountLocators.LAST_NAME).send_keys(lastname)

    def send_email(self, email):
        with allure.step("Проверка поля ввода first name"):
            self.find_element(RegisterAccountLocators.EMAIL).send_keys(email)

    def send_phone(self, phone):
        with allure.step("Проверка поля ввода first name"):
            self.find_element(RegisterAccountLocators.PHONE).send_keys(phone)

    def password(self, password):
        with allure.step("Ввод пароля"):
            self.find_element(RegisterAccountLocators.PASSWORD).send_keys(password)
            self.find_element(RegisterAccountLocators.CONFIRM_PASSWORD).send_keys(password)

    def agree(self):
        with allure.step("Согласие с условиями конфиденциальности"):
            self.find_element(RegisterAccountLocators.AGREE_PRIVACY_POLICY).click()

    def continue_btn(self):
        with allure.step("Нажатие на кнопку продолжить"):
            self.find_element(RegisterAccountLocators.CONTINUE_BTN).click()

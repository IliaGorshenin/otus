from selenium.webdriver.common.by import By
from src.base_page import BasePage
import allure



class AdminLocators:
    IMAGE_OPENCART = (By.XPATH, "//img[@alt='OpenCart']")
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN = (By.XPATH, "//button[text()=' Login']")


class Admin(BasePage):
    def check_image_opencart(self):

        with allure.step("Проверка логотипа на странице"):
            self.find_element(AdminLocators.IMAGE_OPENCART)
            return True

    def check_username(self):
        with allure.step("Проверка поля user name"):
            self.find_element(AdminLocators.USERNAME)
            return True

    def check_password(self):
        with allure.step("Проверка поля password"):
            self.find_element(AdminLocators.PASSWORD)
            return True

    def check_login(self):
        with allure.step("Проверка поля login"):
            self.find_element(AdminLocators.LOGIN)
            return True

    def btn_login(self):
        with allure.step("Нажатие на кнопку login"):
            self.find_element(AdminLocators.LOGIN).click()

    def submit_login(self, name):
        with allure.step("Ввод логина в поле login"):
            self.find_element(AdminLocators.USERNAME).send_keys(name)

    def submit_password(self, password):
        with allure.step("Ввод логина в поле password"):
            self.find_element(AdminLocators.PASSWORD).send_keys(password)

    def check_username(self):
        self.find_element(AdminLocators.USERNAME)
        return True

    def check_password(self):
        self.find_element(AdminLocators.PASSWORD)
        return True

    def check_login(self):
        self.find_element(AdminLocators.LOGIN)
        return True

    def btn_login(self):
        self.find_element(AdminLocators.LOGIN).click()

    def submit_login(self, name):
        self.find_element(AdminLocators.USERNAME).send_keys(name)

    def submit_password(self, password):
        self.find_element(AdminLocators.PASSWORD).send_keys(password)
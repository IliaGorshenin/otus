from selenium.webdriver.common.by import By
from src.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class HomeLocators:
    SEARCH = (By.XPATH, "//input[@name='search']")
    BTN_SEARCH = (By.XPATH, "//i[@class='fa fa-search']")
    DESKTOPS = (By.XPATH, "//*[(text() = 'Desktops')]")
    LOGO = (By.XPATH, "//div[@id='logo']//a[1]")
    PLACEHOLDER_SEARCH = (By.XPATH, "//input[@placeholder='Search']")
    LOGO_BTN_SEARCH = (By.XPATH, "//span[@class='input-group-btn']//button[1]")
    SHOPPING_BASKET = (By.XPATH, "//div[@id='cart']//button[1]")
    SEE_ALL = (By.XPATH, "//a[@class='see-all']")
    MY_ACCOUNT = (By.XPATH, "//a[@title='My Account']")
    BTN_CURRENCY = (By.XPATH, "//strong[text()='$']")


class Home(BasePage):
    def open_my_account(self):
        with allure.step("Нажатие на кнопку Мой аккаунт"):
            self.find_element(HomeLocators.MY_ACCOUNT).click()

    def search_line(self, text):
        with allure.step("Проверка поля login"):
            self.find_element(HomeLocators.SEARCH).send_keys(f"{text}")
            self.find_element(HomeLocators.BTN_SEARCH).click()

    def go_to_desktops(self):
        with allure.step("Выбор раздела desktops"):
            self.find_element(HomeLocators.DESKTOPS).click()

    def check_logo(self):
        with allure.step("Проверка логотипа на странице"):
            self.find_element(HomeLocators.LOGO)
            return True

    def check_placeholder(self):
        with allure.step("Проверка плейсхолдера поисковой строки"):
            self.find_element(HomeLocators.PLACEHOLDER_SEARCH)
            return True

    def check_logo_search(self):
        with allure.step("Проверка наличия логотипа кнопки поиска"):
            self.find_element(HomeLocators.LOGO_BTN_SEARCH)
            return True

    def check_shopping_basket(self):
        with allure.step("Проверка иконки корзины покупок"):
            self.find_element(HomeLocators.SHOPPING_BASKET)
            return True

    def see_all(self):
        with allure.step("Нажатие на кнопку просмотра всех товаров"):
            self.find_element(HomeLocators.SEE_ALL).click()

    def currency(self, name):
        with allure.step("Смена валюты"):
            self.find_element(HomeLocators.BTN_CURRENCY).click()
            self.find_element(By.NAME, f"{name}")

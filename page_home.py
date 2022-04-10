from selenium.webdriver.common.by import By
from src.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        self.find_element(HomeLocators.MY_ACCOUNT).click()

    def search_line(self, text):
        self.find_element(HomeLocators.SEARCH).send_keys(f"{text}")
        self.find_element(HomeLocators.BTN_SEARCH).click()

    def go_to_desktops(self):
        self.find_element(HomeLocators.DESKTOPS).click()

    def check_logo(self):
        self.find_element(HomeLocators.LOGO)
        return True

    def check_placeholder(self):
        self.find_element(HomeLocators.PLACEHOLDER_SEARCH)
        return True

    def check_logo_search(self):
        self.find_element(HomeLocators.LOGO_BTN_SEARCH)
        return True

    def check_shopping_basket(self):
        self.find_element(HomeLocators.SHOPPING_BASKET)
        return True

    def see_all(self):
        self.find_element(HomeLocators.SEE_ALL).click()

    def currency(self, name):
        self.find_element(HomeLocators.BTN_CURRENCY).click()
        self.find_element(By.NAME, f"{name}")

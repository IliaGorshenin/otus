import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def search_for_text_on_page(self, text):
        self.browser.find_element(By.XPATH, f"//*[(text() = '{text}')]")
        return True

    def open_search_for_text_element(self, text):
        self.browser.find_element(By.XPATH, f"//*[(text() = '{text}')]").click()

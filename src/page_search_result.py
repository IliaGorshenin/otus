from selenium.webdriver.common.by import By
from src.base_page import BasePage
import allure


class SearchResultLocators:
    IMAGE_ELEMENT = (By.XPATH, "//img[@alt='iMac']")
    ADD_WISH_LIST = (By.XPATH, "(//i[@class='fa fa-heart'])[2]")
    COMPARE = (By.XPATH, "//i[@class='fa fa-exchange']")
    ADD_TO_CART = (By.ID, "button-cart")
    SORT_BY = (By.ID, "input-sort")
    LIMIT_ON_PAGE = (By.ID, "input-limit")
    LIST_VIEW = (By.ID, "list-view")
    GRID_VIEW = (By.ID, "grid-view")


class SearchResult(BasePage):
    def open_element(self):
        with allure.step("Нажатие на логотип элемента"):
            self.find_element(SearchResultLocators.IMAGE_ELEMENT).click()

    def add_to_wish_list(self):
        with allure.step("Проверка наличия иконки добавления товара в избранное"):
            self.find_element(SearchResultLocators.ADD_WISH_LIST)
            return True

    def check_btn_compare(self):
        with allure.step("Проверка наличия иконки добавления товара в сравнение"):
            self.find_element(SearchResultLocators.COMPARE)
            return True

    def add_to_cart(self):
        with allure.step("Проверка наличия иконки добавления товара в избранное"):
            self.find_element(SearchResultLocators.ADD_TO_CART)
            return True

    def check_sort(self):
        with allure.step("Проверка наличия иконки добавления товара в корзину"):
            self.find_element(SearchResultLocators.SORT_BY)
            return True

    def check_input_limit(self):
        with allure.step("Проверка наличия иконки добавления товара в избранное"):
            self.find_element(SearchResultLocators.LIMIT_ON_PAGE)
            return True

    def add_to_wish_list(self):
        self.find_element(SearchResultLocators.ADD_WISH_LIST)
        return True

    def check_btn_compare(self):
        self.find_element(SearchResultLocators.COMPARE)
        return True

    def add_to_cart(self):
        self.find_element(SearchResultLocators.ADD_TO_CART)
        return True

    def check_sort(self):
        self.find_element(SearchResultLocators.SORT_BY)
        return True

    def check_input_limit(self):
        self.find_element(SearchResultLocators.LIMIT_ON_PAGE)
        return True

    def check_list_view(self):
        self.find_element(SearchResultLocators.LIST_VIEW)
        return True

    def check_grid_view(self):
        self.find_element(SearchResultLocators.GRID_VIEW)
        return True

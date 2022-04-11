from selenium.webdriver.common.by import By
from src.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminNavigationLocators:
    ADD_BTN = (By.XPATH, "//a[@class='btn btn-primary']")
    NAME_PRODUCT = (By.XPATH, "//label[text()='Product Name']/following::input")
    DESCRIPTION = (By.XPATH, "//textarea[@class='note-codable']/following-sibling::div[1]")
    BTN_SAVE = (By.XPATH, "//i[@class='fa fa-save']")
    META_TAG = (By.ID, "input-meta-title1")
    CATALOG = (By.XPATH, "//a[@class='parent collapsed']")
    PRODUCTS = (By.XPATH, "//ul[@id='collapse1']/li[2]/a[1]")
    DATA_PRODUCT = (By.LINK_TEXT, "Data")
    MODEL_PRODUCT = (By.ID, "input-model")
    EDIT_PRODUCT_BTN = (By.XPATH, "//form[@id='form-product']/div[1]/table[1]/tbody[1]/tr[20]/td[8]/a[1]")
    DELETE_PRODUCT_BTN = (By.XPATH, "//button[@class='btn btn-danger']")
    CHECKBOX_ELEMENT = (By.XPATH, "//form[@id='form-product']/div[1]/table[1]/tbody[1]/tr[20]/td[1]/input[1]")


class AdminNavigation(BasePage):
    def submit_name(self, name):
        self.find_element(AdminNavigationLocators.NAME_PRODUCT).send_keys(name)

    def submit_description(self, description):
        self.find_element(AdminNavigationLocators.DESCRIPTION).send_keys(description)

    def submit_meta_tag(self, tag):
        self.find_element(AdminNavigationLocators.META_TAG).send_keys(tag)

    def save_new_product(self):
        self.find_element(AdminNavigationLocators.BTN_SAVE).click()

    def open_catalog(self):
        self.find_element(AdminNavigationLocators.CATALOG).click()

    def open_products(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(AdminNavigationLocators.PRODUCTS)).click()

    def add_new_product(self):
        self.find_element(AdminNavigationLocators.ADD_BTN).click()

    def open_data_product(self):
        self.find_element(AdminNavigationLocators.DATA_PRODUCT).click()

    def submit_model(self, model):
        self.find_element(AdminNavigationLocators.MODEL_PRODUCT).send_keys(model)

    def edit_product(self):
        self.find_element(AdminNavigationLocators.EDIT_PRODUCT_BTN).click()

    def checkbox(self):
        self.find_element(AdminNavigationLocators.CHECKBOX_ELEMENT).click()

    def delete_product(self):
        self.find_element(AdminNavigationLocators.DELETE_PRODUCT_BTN).click()

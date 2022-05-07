from src.page_admin import Admin
from src.page_admin_navigation import AdminNavigation
from src.base_page import BasePage
import allure


@allure.feature('Тесты для продуктов')
@allure.story('Добавление нового продукта в каталог')
def test_add_product(browser):
    browser.get('https://demo.opencart.com/admin/')
    name_product = "Test_name_1"
    Admin(browser).submit_login("user")
    Admin(browser).submit_password("bitnami")
    Admin(browser).btn_login()
    AdminNavigation(browser).open_catalog()
    AdminNavigation(browser).open_products()
    AdminNavigation(browser).add_new_product()
    AdminNavigation(browser).submit_name(name_product)
    AdminNavigation(browser).submit_description("Test_description")
    AdminNavigation(browser).submit_meta_tag("Test_meta_tag_1")
    AdminNavigation(browser).open_data_product()
    AdminNavigation(browser).submit_model("Test_model_1")
    AdminNavigation(browser).save_new_product()
    assert BasePage(browser).search_for_text_on_page(name_product)

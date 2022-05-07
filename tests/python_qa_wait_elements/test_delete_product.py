from src.page_admin import Admin
from src.page_admin_navigation import AdminNavigation
from src.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


@allure.feature('Тесты на продукты')
@allure.story('Удаление продукта из каталога')
def test_delete_product(browser):
    name_product = "Test_name"
    Admin(browser).submit_login("user")
    Admin(browser).submit_password("bitnami")
    Admin(browser).btn_login()
    AdminNavigation(browser).open_catalog()
    AdminNavigation(browser).open_products()
    try:
        assert BasePage(browser).search_for_text_on_page(name_product)
        AdminNavigation(browser).checkbox()
        AdminNavigation(browser).delete_product()
        confirm = browser.switch_to.alert
        confirm.accept()
    except NoSuchElementException:
        AdminNavigation(browser).add_new_product()
        AdminNavigation(browser).submit_name(name_product)
        AdminNavigation(browser).submit_description("Test_description")
        AdminNavigation(browser).submit_meta_tag("Test_meta_tag")
        AdminNavigation(browser).open_data_product()
        AdminNavigation(browser).submit_model("Test_model")
        AdminNavigation(browser).save_new_product()
        assert BasePage(browser).search_for_text_on_page(name_product)
        AdminNavigation(browser).checkbox()
        AdminNavigation(browser).delete_product()
        confirm = browser.switch_to.alert
        confirm.accept()

from src.page_admin import Admin
from src.page_admin_navigation import AdminNavigation
from src.base_page import BasePage


def test_add_product(browser):
    browser.get("http://192.168.0.15:8081/admin")
    name_product = "Test_name"
    Admin(browser).submit_login("user")
    Admin(browser).submit_password("bitnami")
    Admin(browser).btn_login()
    AdminNavigation(browser).open_catalog()
    AdminNavigation(browser).open_products()
    AdminNavigation(browser).add_new_product()
    AdminNavigation(browser).submit_name(name_product)
    AdminNavigation(browser).submit_description("Test_description")
    AdminNavigation(browser).submit_meta_tag("Test_meta_tag")
    AdminNavigation(browser).open_data_product()
    AdminNavigation(browser).submit_model("Test_model")
    AdminNavigation(browser).save_new_product()
    assert BasePage(browser).search_for_text_on_page(name_product)

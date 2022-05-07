from src.page_admin import Admin
import allure


@allure.feature('Тесты админки')
@allure.story('Проверка полей входа в панель администратора')
def test_check_login_admin(browser):
    browser.get('https://demo.opencart.com/admin/')
    assert Admin(browser).check_image_opencart()
    assert Admin(browser).check_username()
    assert Admin(browser).check_password()
    assert Admin(browser).check_login()

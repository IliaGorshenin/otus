from src.base_page import BasePage
from src.page_home import Home
from src.page_register_account import RegisterAccount
import allure


@allure.feature('Тесты на аккаунты')
@allure.story('Создание нового аккаунта')
def test_register_new_account(browser):
    Home(browser).open_my_account()
    BasePage(browser).open_search_for_text_element('Register')
    RegisterAccount(browser).send_first_name("Сидоров")
    RegisterAccount(browser).send_last_name("Иван")
    RegisterAccount(browser).send_email("test54321@mail.ru")
    RegisterAccount(browser).send_phone("+74959876543")
    RegisterAccount(browser).password("qwert123")
    RegisterAccount(browser).agree()
    RegisterAccount(browser).continue_btn()
    assert BasePage(browser).search_for_text_on_page("Your Account Has Been Created!")


@allure.feature('Тесты на аккаунты')
@allure.story('Проверка полей при регистрации нового пользователя')
def test_check_register(browser):
    Home(browser).open_my_account()
    BasePage(browser).open_search_for_text_element('Register')
    assert RegisterAccount(browser).check_input_first_name()
    assert RegisterAccount(browser).check_input_last_name()
    assert RegisterAccount(browser).check_email()

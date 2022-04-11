from src.base_page import BasePage
from src.page_home import Home
from src.page_register_account import RegisterAccount


def test_register_new_account(browser):
    Home(browser).open_my_account()
    BasePage(browser).open_search_for_text_element('Register')
    RegisterAccount(browser).send_first_name("Магистр")
    RegisterAccount(browser).send_last_name("Йода")
    RegisterAccount(browser).send_email("test1589@mail.ru")
    RegisterAccount(browser).send_phone("+74951234567")
    RegisterAccount(browser).password("qwert123")
    RegisterAccount(browser).agree()
    RegisterAccount(browser).continue_btn()
    assert BasePage(browser).search_for_text_on_page("Your Account Has Been Created!")


def test_check_register(browser):
    Home(browser).open_my_account()
    BasePage(browser).open_search_for_text_element('Register')
    assert RegisterAccount(browser).check_input_first_name()
    assert RegisterAccount(browser).check_input_last_name()
    assert RegisterAccount(browser).check_email()

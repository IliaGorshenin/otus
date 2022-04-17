from src.page_home import Home
import allure


@allure.feature('Тесты на главной странице')
@allure.story('Смена валюты')
def currency_selection(browser):
    browser.get('https://demo.opencart.com')
    Home(browser).currency("EUR")
    Home(browser).currency("GBP")
    Home(browser).currency("USD")


@allure.feature('Тесты на главной странице')
@allure.story('Проверка логотипа, плейсхолдера поиска, иконки поиска и иконки корзины')
def test_check_home(browser):
    browser.get('https://demo.opencart.com')
    assert Home(browser).check_logo()
    assert Home(browser).check_placeholder()
    assert Home(browser).check_logo_search()
    assert Home(browser).check_shopping_basket()

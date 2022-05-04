from src.page_home import Home
import allure


@allure.feature('Тесты на главной странице')
@allure.story('Смена валюты')
def test_currency_selection(browser):
    Home(browser).currency("EUR")
    Home(browser).currency("GBP")
    Home(browser).currency("USD")


@allure.feature('Тесты на главной странице')
@allure.story('Проверка логотипа, плейсхолдера поиска, иконки поиска и иконки корзины')
def test_check_home(browser):
    assert Home(browser).check_logo()
    assert Home(browser).check_placeholder()
    assert Home(browser).check_logo_search()
    assert Home(browser).check_shopping_basket()

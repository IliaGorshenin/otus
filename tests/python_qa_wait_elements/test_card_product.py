from src.page_home import Home
from src.page_search_result import SearchResult
import allure


@allure.feature('Тесты на карточки товаров')
@allure.story('Проверка иконок на карточке товара')
def test_check_card_product(browser):
    browser.get('https://demo.opencart.com')
    Home(browser).search_line('mac')
    SearchResult(browser).open_element()
    assert SearchResult(browser).add_to_wish_list()
    assert SearchResult(browser).check_btn_compare()
    assert SearchResult(browser).add_to_cart()

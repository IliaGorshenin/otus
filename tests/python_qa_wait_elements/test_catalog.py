from src.page_home import Home
from src.page_search_result import SearchResult
import allure


@allure.feature('Тесты на аккаунты')
@allure.story('Создание нового аккаунта')
def test_check_catalog(browser):
    browser.get('https://demo.opencart.com')
    Home(browser).go_to_desktops()
    Home(browser).see_all()
    assert SearchResult(browser).check_sort()
    assert SearchResult(browser).check_input_limit()
    assert SearchResult(browser).check_list_view()
    assert SearchResult(browser).check_grid_view()

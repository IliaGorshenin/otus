from src.page_home import Home
from src.page_search_result import SearchResult


def test_check_card_product(browser):
    Home(browser).search_line('mac')
    SearchResult(browser).open_element()
    assert SearchResult(browser).add_to_wish_list()
    assert SearchResult(browser).check_btn_compare()
    assert SearchResult(browser).add_to_cart()

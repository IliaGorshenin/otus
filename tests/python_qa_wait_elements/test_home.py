from src.page_home import Home


def currency_selection(browser):
    Home(browser).currency("EUR")
    Home(browser).currency("GBP")
    Home(browser).currency("USD")


def test_check_home(browser):
    assert Home(browser).check_logo()
    assert Home(browser).check_placeholder()
    assert Home(browser).check_logo_search()
    assert Home(browser).check_shopping_basket()


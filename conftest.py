import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="localhost:8081")


@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Opera()

    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.close)
    return driver

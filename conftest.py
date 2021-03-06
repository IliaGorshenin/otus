import datetime
import os
import time
from pathlib import Path
import allure
import pytest
from selenium import webdriver
import logging
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def directory_log():
    path = (Path.cwd() / "logs")
    if os.path.exists(path):
        print("Директория найдена")
    else:
        os.mkdir(path)
        print("Директория создана")
    return path


logging.basicConfig(handlers=[logging.FileHandler(filename=directory_log() / "test.log", encoding='utf-8')],
                    datefmt="%F %A %T",
                    format="[%(asctime)s] %(name)s:%(levelname)s:%(message)s",
                    level=logging.INFO)


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.info(f"I'm navigating to {url} and {driver.title}")

    def after_navigate_to(self, url, driver):
        logging.info(f"I'm on {url}")

    def before_navigate_back(self, driver):
        logging.info(f"I'm navigating back")

    def after_navigate_back(self, driver):
        logging.info(f"I'm back!")

    def before_find(self, by, value, driver):
        logging.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logging.info(f"I've found '{value}' with '{by}'")

    def before_click(self, element, driver):
        logging.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"I've clicked {element}")

    def before_execute_script(self, script, driver):
        logging.info(f"I'm executing '{script}'")

    def after_execute_script(self, script, driver):
        logging.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        logging.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        logging.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        logging.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'logs/{driver.session_id}.png')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--executor", default="192.168.0.15")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--bversion")
    parser.addoption("--url", default="https://demo.opencart.com")



@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")
    mobile = request.config.getoption("--mobile")
    logger = logging.getLogger('driver')
    test_name = request.node.name
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        if mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", desired_capabilities=caps)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'goog:chromeOptions': {}
        }

        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

        if not mobile:
            driver.maximize_window()

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name
    driver.log_level = log_level
    driver.get(url)
    logger.info(driver)

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    driver.maximize_window()
    request.addfinalizer(fin)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    current_date = datetime.datetime.now()
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed or rep.skipped:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            time.sleep(2)
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name=f'screenshot {current_date}',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

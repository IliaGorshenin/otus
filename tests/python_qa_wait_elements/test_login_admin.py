from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_login_admin(browser):
    browser.get('https://demo.opencart.com/admin/')
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='OpenCart']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login']")))



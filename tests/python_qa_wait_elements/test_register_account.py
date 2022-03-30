from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_register(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element(By.XPATH, "//a[@title='My Account']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[(text() = 'Register')]"))).click()
    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))

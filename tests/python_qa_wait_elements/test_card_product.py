from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_card_product(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element(By.XPATH, "//input[@name='search']").send_keys('mac')
    browser.find_element(By.XPATH, "//i[@class='fa fa-search']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='iMac']"))).click()
    wait.until(EC.title_is("iMac"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-toggle='tooltip']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-exchange']")))
    wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_catalog(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element(By.XPATH, "//*[(text() = 'Desktops')]").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='see-all']"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "input-sort")))
    wait.until(EC.element_to_be_clickable((By.ID, "input-limit")))
    wait.until(EC.visibility_of_element_located((By.ID, "list-view")))
    wait.until(EC.visibility_of_element_located((By.ID, "grid-view")))

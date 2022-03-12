from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_home(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='logo']//a[1]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='input-group-btn']//button[1]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='cart']//button[1]")))

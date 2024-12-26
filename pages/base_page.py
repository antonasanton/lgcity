from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    def get_text(self, by: By, value: str):
        return self.driver.find_element(by, value).text
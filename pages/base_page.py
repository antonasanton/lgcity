from selenium import webdriver

from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def click(self, by: By, value: str):
        self.find_element(by, value).click()


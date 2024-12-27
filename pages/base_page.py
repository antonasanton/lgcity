from selenium import webdriver
import allure
import time
import random
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @allure.step("Открытие браузера")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Поиск элемента")
    # def find_element(self, by: By, value: str):
    #     return self.driver.find_element(by, value)
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Нажатие на элемент")
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step("Получение текста")
    def get_text(self, by: By, value: str):
        return self.driver.find_element(by, value).text

    @allure.step("Подсчет элементов")
    def count_element(self, locator):
        return len(self.find_element(locator))

    @allure.step("Нажатие Enter")
    def  press_enter(self, subjects):
        element = self.find_element(subjects)
        element.send_keys(Keys.ENTER)

    @allure.step("Скриншот")
    def get_screenshot(self):
        allure.attach(
            name="Скриншот",
            body=self.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
    @allure.step("Возврат на предидущую страницу")
    def go_to_previous_page(self):
        self.driver.back()
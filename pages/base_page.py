from selenium import webdriver
import allure
import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# class BasePage:
#     def __init__(self, driver: webdriver.Chrome):
#         self.driver = driver

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Закрытие уведомления о Куках")
    def close_cookie(self):
        self.driver.find_element(By.XPATH, "//button[@class = 'button button--fill button--cookie-close']").click()

    @allure.step("Открытие браузера")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Поиск элемента")
    # def find_element(self, by: By, value: str):
    #     return self.driver.find_element(by, value)
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Нажатие на элемент")
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step("Получение текста")
    # def get_text(self, by: By, value: str):
    #     return self.driver.find_element(by, value).text
    def get_text(self, locator):
        return self.find_element(locator).text

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

    @allure.step("Нажатие на ранжомный элемент")
    def click_random_element(self, locator):
        random.choice(self.find_elements(locator)).click()

    def get_random_element(self, locator):
        return random.choice(self.find_elements(locator))

    def count_elements(self, locator):
        return len(self.find_elements(locator))

    def open_cart(self):
        self.click((By.XPATH, "//header[@class='header']//a[@data-popup='popup--basket']"))
        self.find_element((By.XPATH, "//div[@class='basket__title']"))

    def type_of_product(self):
        self.find_element((By.XPATH, "//span[@itemprop='description']"))


    def close_wheel(self):
        self.find_element((By.XPATH, "//div[contains(@style, 'flex')]/iframe[@title='Flocktory widget']"))
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//div[contains(@style, 'flex')]/iframe[@title='Flocktory widget']"))
        self.find_element((By.XPATH, "//button[@class='close js-close']"))
        self.driver.find_element(By.XPATH, "//button[@class='close js-close']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='close js-close']").click()
        self.driver.switch_to.default_content()
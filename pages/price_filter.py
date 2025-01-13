import allure
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage


class PriceFilter(BasePage):
    CATALOG_URL = "https://lgcity.ru/outerwear/women/"
    price_field = (By.XPATH, "//div[@class='filter__input-subtitle' and contains(text(), '₽')]")
    price_input_from = (By.XPATH, "//input[@class='filter__slider-input filter__slider-input--from']")
    price_input_to = (By.XPATH, "//input[@class='filter__slider-input filter__slider-input--to']")
    show_btn = (By.XPATH, "//span[@class='js-show-count-text']")
    prices = (By.XPATH, "//div[@itemprop='price']")

    @allure.step("Открытие каталога")
    def open_catalog(self):
        self.open(self.CATALOG_URL)

    @allure.step("Фильтр по цене")
    def add_price_filter(self):
        self.click(self.price_field)
        self.press_cmd_backspace(self.price_input_from)
        self.enter_text(self.price_input_from, "3000")
        self.press_enter(self.price_input_from)
        self.press_cmd_backspace(self.price_input_to)
        self.enter_text(self.price_input_to, "6000")
        self.press_enter(self.price_input_to)
        self.click(self.show_btn)
        time.sleep(3)

    def get_prices(self, locator):
        prices = []
        list_of_prices = self.find_elements(self.prices)

        for i in list_of_prices:
            text = i.text.strip()
            clean_price = text.replace(' ', '').replace('₽', '')
            prices.append(clean_price)
        return prices


    def check_prices(self, list_a):
        for i in list_a:
            assert int(i) >= 3000 <= 6000

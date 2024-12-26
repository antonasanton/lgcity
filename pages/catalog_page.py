import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CatalogPage(BasePage):
    CATALOG_URL = "https://lgcity.ru/outerwear/women/"

    def open_catalog(self):
        self.open(self.CATALOG_URL)

    def close_cookie(self):
        self.driver.find_element(By.XPATH,"//button[@class = 'button button--fill button--cookie-close']").click()


    def open_random_product(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='catalog__item-title']")))
        time.sleep(5)
        self.close_cookie()

        product_cards = self.driver.find_elements(By.XPATH, "//div[@class='catalog__item-title']")
        random_card = random.choice(product_cards)
        self.close_cookie()
        random_card.click()

        self.click((By.XPATH, "//div[@id='btn-add-to-favorite-text' and contains(@class, 'card__info-favorite-text')]"))
        self.click((By.XPATH, "//a[contains(@class, 'header__r-icons-link--favorite')]"))





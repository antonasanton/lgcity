import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CatalogPage(BasePage):
    CATALOG_URL = "https://lgcity.ru/outerwear/women/48/6pm/"

    def open_catalog(self):
        self.open(self.CATALOG_URL)

    def open_random_product(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'swiper-slide')]")))

        product_cards = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'swiper-slide') and contains(@class, 'swiper-slide-active')]")
        random_card = random.choice(product_cards)
        random_card.click()


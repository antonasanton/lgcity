import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

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

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//section[@class='widget js-widget']//button[@class='close']")))
        block_button = self.find_element(By.XPATH, "//button[contains(text(), 'Блокировать')]")
        block_button.click()


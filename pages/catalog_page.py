import random
import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CatalogPage(BasePage):
    CATALOG_URL = "https://lgcity.ru/outerwear/women/"

    @allure.step("Открытие каталога")
    def open_catalog(self):
        self.open(self.CATALOG_URL)



    @allure.step("Открытие рандомной карточки товара")
    def open_random_product(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='catalog__item-title']")))
        time.sleep(5)
        self.close_cookie()
        product_cards = self.driver.find_elements(By.XPATH, "//div[@class='catalog__item-title']")
        random_card = random.choice(product_cards)
        random_card.click()

        name = self.driver.find_element(By.XPATH,"//a[@class = 'card__info-link']").text
        type = self.driver.find_element(By.XPATH,"//span[@class = 'card__info-desc']").text
        time.sleep(3)
        price = self.driver.find_element(By.XPATH,"//div[@class = 'card__info-price-text card__info-price-text--new']").text

        self.click((By.XPATH, "//div[@id='btn-add-to-favorite-text' and contains(@class, 'card__info-favorite-text')]"))
        time.sleep(2)
        self.click((By.XPATH, "//a[contains(@class, 'header__r-icons-link--favorite')]"))

        name_fav = self.driver.find_element(By.XPATH,"//div[@class = 'catalog__item-title']").text
        type_fav = self.driver.find_element(By.XPATH,"//div[@class = 'catalog__item-desc']").text
        time.sleep(3)
        price_fav = self.driver.find_element(By.XPATH, "//div[@class='catalog__item-price']//div[@class='catalog__item-price-new' and @itemprop='price']").text

        assert name == name_fav
        assert type == type_fav
        assert price == price_fav




 
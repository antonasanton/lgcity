import random
import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class WeelClose(BasePage):
    CATALOG_URL = "https://lgcity.ru/outerwear/women/"

    def open_catalog(self):
        self.open(self.CATALOG_URL)


    def open_random_product(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='catalog__item-title']")))
        time.sleep(1)
        self.close_cookie()

        product_cards = self.driver.find_elements(By.XPATH, "//div[@class='catalog__item-title']")

        random_card = random.choice(product_cards)
        random_card.click()

        time.sleep(5)
        self.go_to_previous_page()
        time.sleep(10)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close js-close' and @style='opacity: 0.5;']")))

        close_button = self.driver.find_elements(By.XPATH,"//button[@class='close js-close' and @style='opacity: 0.5;']")
        if close_button:
            close_button[0].click()
            time.sleep(2)
            close_button[0].click()
        else:
            print("Кнопка закрытия не найдена")

            time.sleep(5)


        # self.driver.find_elements(By.XPATH, "//button[@class='close js-close' and @style='opacity: 0.5;']").click()
        # WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='close js-close' and @style='opacity: 0.5;']")))



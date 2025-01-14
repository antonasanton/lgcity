import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import requests
import allure

BASE_URL = 'https://www.citilink.ru/'

class MVideo(BasePage):

    # CITY = (By.XPATH, "//div[@class='location-deny link link--blue']")
    # YES_CITY = (By.XPATH, "//div[@class='mv-main-button--content' and text()=' Все верно ']")
    CATALOG_BTN = (By.XPATH, "//span[@class='app-catalog-19y4hmw e1fnp08x0' and text()='Каталог товаров']")
    SMARTPHONE_BTN = (By.XPATH, "//a[@class='app-catalog-yhixh0 euu8i7z0' and text()='Смартфоны и планшеты']")
    SMARTPHONES_AND_PHONES_BTN = (By.XPATH, "//span[@class='app-catalog-pt72uc e66p2eb0' and text()='Смартфоны']")
    # SMARTPHONES_BTN = (By.XPATH, "//div[@class='fl-category__title' and text()='Смартфоны']")
    LIST_OF_PHONES = (By.XPATH, "//a[@class='app-catalog-9gnskf e1259i3g0']")
    COOKIE_CLOSE_BTN = (By.XPATH, "//button[@class ='e4uhfkv0 app-catalog-1lxdbiq e4mggex0']")
    ITEM_NAME = (By.XPATH, "//h1[@class='easmdi50 eml1k9j0 app-catalog-lc5se5 e1gjr6xo0']")
    ITEM_PRICE = (By.XPATH, "//span[@class='e1j9birj0 e106ikdt0 app-catalog-8hy98m e1gjr6xo0']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@class ='e11w80q30 e4uhfkv0 app-catalog-zkoen2 e4mggex0']")
    GO_TO_CART_BTN = (By.XPATH, "(//a[contains(@class,'app-catalog-1k0cnlg') and @href='/order/']/button/span[contains(text(), 'Перейти в корзину')])[1]")
    ITEM_NAME_IN_CART = (By.XPATH, "//span[@class ='e1ys5m360 e106ikdt0 css-56qww8 e1gjr6xo0']")
    ITEM_PRICE_IN_CART = (By.XPATH, "//span[@class='e1j9birj0 e106ikdt0 css-1spb733 e1gjr6xo0']")


    def open_main_page(self):
        self.open(BASE_URL)

    def get_name_from_item(self):
        return self.find_element(self.ITEM_NAME).text

    def get_price_from_item(self):
        return self.find_element(self.ITEM_PRICE).text

    def get_name_from_cert(self):
        return self.find_element(self.ITEM_NAME_IN_CART).text

    def get_price_from_cert(self):
        return self.find_element(self.ITEM_PRICE_IN_CART).text

    def open_catalog(self):
        self.click(self.CATALOG_BTN)
        self.click(self.SMARTPHONE_BTN)
        self.click(self.COOKIE_CLOSE_BTN)
        self.click(self.SMARTPHONES_AND_PHONES_BTN)
        time.sleep(1)
        self.click_random_element(self.LIST_OF_PHONES)
        time.sleep(1)
        self.get_name_from_item()
        self.get_price_from_item()
        self.click(self.ADD_TO_CART_BTN)
        self.click(self.GO_TO_CART_BTN)
        self.get_name_from_cert()
        self.get_price_from_cert()

    def check_data(self):
        item_name, item_price, cert_name, cert_price = self.open_catalog()
        assert item_name == cert_name, f"Expected {item_name}, but got {cert_name}"
        assert item_price == cert_price, f"Expected {item_price}, but got {cert_price}"
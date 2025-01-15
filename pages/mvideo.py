from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

BASE_URL = 'https://www.citilink.ru/'

class MVideo(BasePage):

    CATALOG_BTN = (By.XPATH, "//a[@data-meta-name='DesktopHeaderFixed__catalog-menu']")  #//span[@class='app-catalog-19y4hmw e1fnp08x0' and text()='Каталог товаров']
    SMARTPHONE_BTN = (By.XPATH, "//a[@class='app-catalog-yhixh0 euu8i7z0' and text()='Смартфоны и планшеты']")
    SMARTPHONES_AND_PHONES_BTN = (By.XPATH, "//div[@data-meta-name='CategoryCardsLayout']//span[contains(text(), 'Смартфоны')]")
    LIST_OF_PHONES = (By.XPATH, "//div[@data-meta-name='SnippetProductHorizontalLayout']//a")
    COOKIE_CLOSE_BTN = (By.XPATH, "//span[contains(text(), 'Я согласен')]")
    ITEM_NAME = (By.XPATH, "//div[@data-meta-name='ProductHeaderLayout__title']")
    ITEM_PRICE = (By.XPATH, "//div[@data-meta-name='PriceBlock__price']//span[@data-meta-is-total='notTotal']//span")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@data-meta-name='BasketDesktopButton']")
    GO_TO_CART_BTN = (By.XPATH,"(//a[@href='/order/']//button[@type='button' and @data-meta-disabled='false'])[1]")
    ITEM_NAME_IN_CART = (By.XPATH, "//div[@data-meta-type='Product']//a")
    ITEM_PRICE_IN_CART = (By.XPATH, "//div[@data-meta-name='BasketSummary']//span[@data-meta-is-total='notTotal']//span")
    QUANTITY_ELEMENT = (By.XPATH, "//input[@data-meta-name='Count__input']")


    def open_main_page(self):
        self.open(BASE_URL)

    def get_name_from_item(self):
        return self.find_element(self.ITEM_NAME).text

    def get_price_from_item(self):
        return self.find_element(self.ITEM_PRICE).text

    def get_name_from_cart(self):
        return self.find_element(self.ITEM_NAME_IN_CART).text

    def get_price_from_cart(self):
        return self.find_element(self.ITEM_PRICE_IN_CART).text

    def get_total_price(self):
        price_text = self.get_price_from_cart()
        price = float(price_text.replace('₽', '').replace(' ', '').replace(',', '.'))
        quantity_element = self.find_element(self.QUANTITY_ELEMENT)
        quantity = int(quantity_element.get_attribute("value"))
        return price * quantity

    def open_catalog_and_add_to_cart(self):
        self.click(self.CATALOG_BTN)
        self.wait.until(EC.visibility_of_element_located(self.SMARTPHONE_BTN))
        self.click(self.SMARTPHONE_BTN)
        self.wait.until(EC.visibility_of_element_located(self.COOKIE_CLOSE_BTN))
        self.click(self.COOKIE_CLOSE_BTN)
        self.click(self.SMARTPHONES_AND_PHONES_BTN)
        self.wait.until(EC.visibility_of_all_elements_located(self.LIST_OF_PHONES))
        self.click_random_element(self.LIST_OF_PHONES)
        self.wait.until(EC.presence_of_element_located(self.ITEM_NAME))
        # self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME))
        item_name = self.get_name_from_item()
        item_price = self.get_price_from_item()
        self.click(self.ADD_TO_CART_BTN)
        self.wait.until(EC.element_to_be_clickable(self.GO_TO_CART_BTN))
        self.click(self.GO_TO_CART_BTN)

        return item_name, item_price

    def check_data(self, item_name, item_price):
        cart_name = self.get_name_from_cart()
        cart_price = self.get_price_from_cart()

        assert item_name == cart_name, (
            f"Ошибка: Название товара не совпадает.\n"
            f"Ожидаемое: {item_name}\n"
            f"Фактическое: {cart_name}"
        )

        assert item_price == cart_price, (
            f"Ошибка: Цена товара не совпадает.\n"
            f"Ожидаемая: {item_price} ₽\n"
            f"Фактическая: {cart_price} ₽"
        )

        total_price = float(self.get_total_price())
        print(
            f"Сравнение прошло успешно!\n"
            f"Название товара: {item_name}, Цена: {item_price} ₽\n"
            f"Общая сумма в корзине: {total_price} ₽"
        )
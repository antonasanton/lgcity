import time, re

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LGCityCart(BasePage):
    cart_product_name = (By.XPATH, "//div[@class='basket__item-title']")
    cart_product_new_price = (By.XPATH, "//div[contains(@class, 'basket__item-price-num--disc')]")
    cart_product_old_price = (By.XPATH, "//div[contains(@class, 'basket__item-price-num--old')]")
    cart_product_type = (By.XPATH, "//p[@class='basket__item-desc']")
    cart_product_size = (By.XPATH, "//div[contains(text(),'Размер:')]")
    cart_product_color = (By.XPATH, "//div[contains(text(),'Цвет:')]")
    cart_product_code = (By.XPATH, "//div[contains(text(),'Код товара:')]")
    cart_overall_sum = (By.ID, "basket-total-price")
    cart_all_elements = (By.XPATH, "//div[@class='basket__item-content']")
    cart_counted_elements = (By.XPATH, "//span[@class='js-basket-product-count']")


    def checking_cart_data(self, size_text, name, type_of_product, new_price, old_price, code, color):
        assert self.get_text(self.cart_product_name) == name, f"Имя товара в карточке не совпало с именем товара в корзине. Имя в карточке - {name}, имя в корзине {self.get_text(self.cart_product_name)}"
        assert self.get_text(self.cart_product_type) == type_of_product, f"Тип товара в карточке не совпал с типом товара в корзине. Тип в карточке - {type_of_product}, тип в корзине {self.get_text(self.cart_product_type)}"
        assert color in self.get_text(self.cart_product_color), f"Цвет товара в карточке не совпал с цветом товара в корзине. Цвет в карточке - {color}, цвет в корзине {self.get_text(self.cart_product_color)}"
        size_from_product_splited = size_text.split(" ")
        size = size_from_product_splited[0]
        country = size_from_product_splited[1]
        assert size in self.find_element(self.cart_product_size).text, f"Размер в корзине не содержит {size}"
        assert country in size_text, f"Страна размера в корзине не содержит {country}"
        assert self.find_element(self.cart_product_new_price).text == new_price, f"Цена со скидкой в карточке не совпала с ценой в корзине. Цена в карточке - {new_price}, цена в корзине {self.find_element(self.cart_product_new_price).text}"
        assert self.find_element(self.cart_product_old_price).text == old_price, f"Цена без скидки в карточке не совпала с ценой в корзине. Цена в карточке - {old_price}, цена в корзине {self.find_element(self.cart_product_old_price).text}"
        assert code in self.find_element(self.cart_product_code).text, f"Код товара в карточке не совпал с кодом в корзине. Код в карточке - {code}, код в корзине {self.find_element(self.cart_product_code).text}"
        time.sleep(0.6)
        numbers_in_cart_product_new_price = re.findall(r'\d+', self.find_element(self.cart_product_new_price).text)
        assert self.find_element(self.cart_overall_sum).text in " ".join(numbers_in_cart_product_new_price), (f"Цена со скидкой не совпала с итоговой ценой. Цена со скидкой - "f"{' '.join(numbers_in_cart_product_new_price)}, итоговая цена {self.find_element(self.cart_overall_sum).text}")
        assert self.count_elements(self.cart_all_elements) == int(self.find_element(self.cart_counted_elements).text), f"Количество товаров в корзине не совпало со счетчиком элементов. Товаров в корзине - {self.count_elements(self.cart_all_elements)}, в счетчике {self.find_element(self.cart_counted_elements).text}"




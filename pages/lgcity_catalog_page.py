import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LGCityCatalog(BasePage):
    products_list = (By.XPATH, "//div[@id='products-list']/a")
    product_name = (By.XPATH, "//a[@class='card__info-link']")
    product_new_price = (By.XPATH, "//div[contains(@class, 'card__info-price-text--new')]")
    product_old_price = (By.XPATH, "//div[contains(@class, 'card__info-price-text--old')]")
    product_type = (By.XPATH, "//div[@class='card__info-title']/span[@class='card__info-desc']")
    product_size = (By.XPATH, "//div[@class='card__info-sizes']/label/div/div")
    product_color = (By.XPATH, "//div[@class='card__color-value']")
    product_code = (By.ID, "offer-artikul")
    btn_add_to_cart = (By.ID, "btn-add-to-cart")

    def forming_cart(self):
        size_text = None
        for i in range(5):
            self.click_random_element(self.products_list)
            self.find_element((By.XPATH, "//label[@class='card__info-size-checkbox ']"))
            if len(self.driver.find_elements(By.XPATH, "//input[@data-can-buy='Y']")) > 0:
                random_size_element = self.get_random_element((By.XPATH, "//input[@data-can-buy='Y']/.."))
                size_text = random_size_element.text
                random_size_element.click()
                time.sleep(2)
                try:
                    self.close_cookie()
                except Exception:
                    pass
                self.find_element(self.btn_add_to_cart)
                self.click(self.btn_add_to_cart)
                break
            else:
                self.go_to_previous_page()
                self.find_element(self.products_list)

        name = self.get_text(self.product_name)
        type_of_product = self.get_text(self.product_type)
        new_price = self.get_text(self.product_new_price)
        old_price = self.get_text(self.product_old_price)
        code = self.get_text(self.product_code)
        color = self.get_text(self.product_color)

        return size_text, name, type_of_product, new_price, old_price, code, color
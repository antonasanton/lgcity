from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import random

BASE_URL = 'https://www.citilink.ru/'

class CitiFilters(BasePage):

    # Локаторы для элементов страницы
    catalog_btn = (By.XPATH, "//a[@data-meta-name='DesktopHeaderFixed__catalog-menu']")  # Кнопка открытия каталога.
    cookie_close_btn = (By.XPATH, "//span[contains(text(), 'Я согласен')]")
    smartphone_btn = (By.XPATH, "//a[@href='/catalog/smartfony/']")  # Кнопка выбора категории 'Смартфоны и планшеты'.
    # SMARTPHONES_AND_PHONES_BTN = (By.XPATH, "//div[@data-meta-name='CategoryCardsLayout']//span[contains(text(), 'Смартфоны')]")  # Кнопка выбора подкатегории 'Смартфоны'.
    filter_brand = (By.XPATH, "//div[@data-meta-value='Бренд']//div[@data-meta-name='FilterGroupLayout']//input")  # Фильтр по бренду.
    filter_memory = (By.XPATH, "//div[@data-meta-value='Оперативная память']//div[@data-meta-name='FilterGroupLayout']//input")  # Фильтр по оперативной памяти.
    filter_screen_resolution = (By.XPATH, "//div[@data-meta-value='Разрешение экрана']//div[@data-meta-name='FilterGroupLayout']//input")  # Фильтр по разрешению экрана.
    applied_filters = (By.XPATH, "//div[contains(@class, 'fresnel-container') and contains(@class, 'fresnel-greaterThanOrEqual-tabletL')]//button/span[not(contains(text(), 'close')) and text() and not(text() = 'Показать все')]")  # Блок с примененными фильтрами.
    product_cards = (By.XPATH, "//div[@data-meta-name='SnippetProductHorizontalLayout']//a")  # Карточки товаров.
    product_details = (By.XPATH, "//ul[contains(@class, 'app-catalog-14f68kq')]//li")  # Детали карточек товаров.

    def open_main_page(self):
        # Открытие главной страницы сайта.
        self.open(BASE_URL)

    def apply_filters_and_check(self):
        self.click(self.catalog_btn)
        self.click(self.cookie_close_btn)
        self.wait.until(EC.visibility_of_element_located(self.smartphone_btn))
        self.click(self.smartphone_btn)

        brand = self.select_random_filter(self.filter_brand)
        memory = self.select_random_filter(self.filter_memory)
        resolution = self.select_random_filter(self.filter_screen_resolution)

        self.wait.until(EC.visibility_of_all_elements_located(self.product_cards))

        applied_filters = [brand, memory, resolution]
        applied_filters_on_page = [filter.text for filter in self.find_elements(self.applied_filters)]

        # Проверка соответствия примененных фильтров с тем, что отображается на странице
        for applied_filter in applied_filters:
            assert applied_filter in applied_filters_on_page, f"Фильтр {applied_filter} отсутствует в списке примененных."

        # Получение характеристик товаров
        product_details = self.get_product_details()

        # Проверка соответствия примененных фильтров с характеристиками товаров
        for applied_filter in applied_filters:
            assert any(applied_filter in details for details in product_details), (
                f"Фильтр {applied_filter} не применился. Отсутствует в характеристиках товаров."
            )

    def select_random_filter(self, filter_locator):
            filters = self.find_elements(filter_locator)
            random_filter = random.choice(filters)
            filter_name = random_filter.get_attribute("value")
            self.click(random_filter)
            return filter_name

    def get_product_details(self):
        product_cards = self.find_elements(self.product_details)
        details = []
        for card in product_cards:
            details.append(card.text)
        return details



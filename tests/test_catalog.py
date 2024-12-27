import time

from pages.catalog_page import CatalogPage
from pages.lgcity_catalog_page import LGCityCatalog
from pages.lgcity_cart_page import LGCityCart
from pages.weel_close import WeelClose


def test_open_random_product(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.open_random_product()
    time.sleep(2)

class TestLGCity:

    def test_lgcity_catalog(self, browser):
        page = LGCityCatalog(browser)
        page.open('https://lgcity.ru/shoes/women/')
        size_text, name, type_of_product, new_price, old_price, code, color = page.forming_cart()
        page.open_cart()
        page = LGCityCart(browser)
        page.checking_cart_data(size_text, name, type_of_product, new_price, old_price, code, color)

    def test_weel_close(self, browser):
        page = WeelClose(browser)
        page.open_catalog()
        page.open_random_product()
        time.sleep(2)
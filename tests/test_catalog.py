import time

from pages.catalog_page import CatalogPage

def test_open_random_product(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_catalog()
    catalog_page.open_random_product()
    time.sleep(2)
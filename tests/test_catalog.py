import time
from pages.catalog_page import CatalogPage
from pages.lgcity_catalog_page import LGCityCatalog
from pages.lgcity_cart_page import LGCityCart
from pages.price_filter import PriceFilter
from pages.petstore_api import PetStoreAPI

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

    def test_price_filter(self, browser):
        page = PriceFilter(browser)
        page.open_catalog()
        page.close_cookie()
        page.add_price_filter()
        list_a = page.get_prices(page.prices)
        page.check_prices(list_a)

def test_petstore_api():
    pet_store = PetStoreAPI()

    new_pet = {
        "id": 1,
        "name": "Vasya",
    }

    pet_store.add_pet(new_pet)
    pet_store.verify_pet_exists(new_pet["id"], new_pet["name"])
    updated_name = "Vasya_updated"
    updated_pet = pet_store.update_pet_name(new_pet, updated_name)
    pet_store.verify_pet_exists(updated_pet["id"], updated_name)
    pet_store.delete_pet(new_pet["id"])

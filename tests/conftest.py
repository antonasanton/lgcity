import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import DEFAULT_TIMEOUT
from pages.register_page import RegisterPage

URL = "https://demoqa.com/automation-practice-form"

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(browser):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(browser, DEFAULT_TIMEOUT)  #явное ожидание

@pytest.fixture
def page_preparation(browser):
        page = RegisterPage(browser, URL)
        (page.open_page_and_checking_url())
        return page

@pytest.fixture(autouse=True)
def cleanup_between_tests(browser):
    yield
    browser.delete_all_cookies()
    browser.refresh()
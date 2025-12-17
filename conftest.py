import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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
    return WebDriverWait(browser, timeout=20)  #явное ожидание


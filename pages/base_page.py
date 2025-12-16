from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import RegisterPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    #открываем нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    #проверяем, что мы на нужной нам странице
    def should_be_correct_url(self):
        assert self.browser.current_url == self.url

    #ожидание появления элемента
    def wait_for_element(self, locator, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    #поиск элемента
    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    #ожидание кликабельности элемента
    def wait_for_clickable(self, locator, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False









from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
import tempfile
import allure

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(DEFAULT_TIMEOUT)

    @allure.step("Открываем страницу и проверяем URL")
    def open_page_and_checking_url(self):
        self.browser.get(self.url)
        assert self.browser.current_url == self.url, \
            f"Expected URL {self.url}, but got {self.browser.current_url}"
        return self

    @allure.step("Ожидаем появление элемента")
    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Применяем ожидание элемента к каждому локатору")
    def is_elements_present(self, *locators):
        for locator in locators:
            element = self.wait_for_element(locator)
            assert element is not None, f"Element {locator} is missing"



    @allure.step("Проверяем отсутствие элемента")
    def is_not_element_present(self, locators, timeout=DEFAULT_TIMEOUT):  # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locators))
        except TimeoutException:
            return True

    @allure.step("Ожидание кликабельности элемента")
    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        click_element =  WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        click_element.click()
        return self

    @allure.step("Создаем временный файл в JPG")
    def create_test_picture(self):
        test_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        test_file.write(b"test image")
        file_path = test_file.name
        test_file.close()
        return file_path



from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
import tempfile

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(DEFAULT_TIMEOUT)

    # открыть страницу
    def open(self):
        self.browser.get(self.url)

    # проверить URL
    def should_be_correct_url(self):
        assert self.browser.current_url == self.url, \
            f"Expected URL {self.url}, but got {self.browser.current_url}"

    # ожидание появления элемента
    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # применяем ожидание элемента к каждому локатору
    def should_be_elements_present(self, *locators):
        for locator in locators:
            element = self.wait_for_element(locator)
            assert element is not None, f"Element {locator} is missing"

    # проверяет presence элемента в DOM (не путать с visibility)
    # отличие от wait_for_element: не ждёт, не проверяет видимость
    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # ожидание кликабельного элемента
    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    #создаем временный файл в jpg
    def create_test_picture(self):
        test_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        test_file.write(b"test image")
        file_path = test_file.name
        test_file.close()
        return file_path


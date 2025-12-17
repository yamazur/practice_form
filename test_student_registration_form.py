import pytest

from pages.locators import RegisterPageLocators
from pages.register_page import RegisterPage
from config import BASE_URL

class TestDisplayingTheRegistrationForm:

    def test_opening_a_page_and_searching_for_elements(self, browser):
        page = RegisterPage(browser, BASE_URL)
        page.open()
        page.should_be_correct_url()
        page.should_be_correct_title()
        page.should_be_elements_present()
        page.should_be_elements_in_login_form()






import pytest
from pages.register_page import RegisterPage

class TestDisplayingTheRegistrationForm:
    def test_opening_a_page_and_searching_for_elements(self, browser):
        page = RegisterPage(browser)
        page.open()
        page.should_be_correct_url()
        page.should_be_login_form()








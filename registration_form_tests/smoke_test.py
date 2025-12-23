import pytest
from pages.register_page import RegisterPage

@pytest.mark.smoke_test
class TestDisplayingTheRegistrationForm:
    def test_displaying_the_registration_form(self, browser):
        page = RegisterPage(browser)
        page.open_page_and_checking_url().should_be_registration_page()

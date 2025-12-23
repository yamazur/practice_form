import pytest
from pages.register_page import RegisterPage

@pytest.mark.negative_test
class TestInvalidRegistration:
    def test_invalid_registration_with_spaces(self, browser):
        page = RegisterPage(browser)
        (page.open_page_and_checking_url()
            .should_be_registration_page()
            .fill_required_with_spaces()
            .fill_valid_optional()
            .click_submit_button()
            .should_not_be_success_message())

    def test_invalid_registration_with_empty_fields(self, browser):
        page = RegisterPage(browser)
        (page.open_page_and_checking_url()
            .should_be_registration_page()
            .fill_valid_optional()
            .click_submit_button()
            .should_not_be_success_message())

from pages.register_page import RegisterPage
from config import BASE_URL
import pytest

@pytest.mark.smoke_test
class TestDisplayingTheRegistrationForm:
    def test_opening_a_page_and_searching_for_elements(self, browser):
        page = RegisterPage(browser, BASE_URL)
        page.open()
        page.should_be_registration_page()

@pytest.mark.positive_test
class TestStudentValidRegistration:
    def test_valid_registration(self, browser):
        page = RegisterPage(browser, BASE_URL)
        page.open()
        page.should_be_registration_page()
        page.valid_required_fields()
        page.valid_optional_fields()
        page.click_submit_button()
        page.should_be_success_message()
        page.should_be_correct_success_message()
        page.modal_close()

@pytest.mark.negative_test
class TestStudentInvalidRegistration:
    def test_required_fields_with_spaces(self, browser):
        page = RegisterPage(browser, BASE_URL)
        page.open()
        page.should_be_registration_page()
        page.fields_filled_with_spaces()
        page.valid_optional_fields()
        page.click_submit_button()
        page.should_not_be_success_message()

    def test_empty_required_fields(self, browser):
        page = RegisterPage(browser, BASE_URL)
        page.open()
        page.should_be_registration_page()
        page.fields_filled_with_spaces()
        page.valid_optional_fields()
        page.click_submit_button()
        page.should_not_be_success_message()

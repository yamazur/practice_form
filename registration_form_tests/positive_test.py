import pytest
from pages.register_page import RegisterPage

@pytest.mark.positive_test
class TestStudentValidRegistration:
    def test_student_valid_registration(self, browser):
        page = RegisterPage(browser)
        (page.open_page_and_checking_url()
            .should_be_registration_page()
            .fill_valid_required()
            .fill_valid_optional()
            .click_submit_button()
            .should_be_success_message()
            .should_be_correct_success_message()
            .modal_close())

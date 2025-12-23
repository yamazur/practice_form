import pytest

@pytest.mark.smoke_test
class TestDisplayingTheRegistrationForm:
    def test_searching_for_elements(self, browser, page_preparation):
        page_preparation.should_be_registration_page()

@pytest.mark.positive_test
class TestStudentValidRegistration:
    def test_valid_registration(self, browser, page_preparation):
        (page_preparation
            .fill_valid_required()
            .fill_valid_optional()
            .click_submit_button())

        page_preparation.should_be_success_message()
        page_preparation.should_be_correct_success_message()

        page_preparation.modal_close()

@pytest.mark.negative_test
class TestStudentInvalidRegistration:
    def test_required_fields_with_spaces(self, browser, page_preparation):
        (page_preparation
            .fill_required_with_spaces()
            .fill_valid_optional()
            .click_submit_button()
            .should_not_be_success_message())

    def test_empty_required_fields(self, browser, page_preparation):
        (page_preparation
            .fill_valid_optional()
            .click_submit_button()
            .should_not_be_success_message())

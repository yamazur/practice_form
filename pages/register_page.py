from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import RegisterPageLocators


class RegistrationPage(BasePage):

    # проверяем, что заголовок страницы (title) соответствует ожидаемому значению
    def should_be_correct_title(self):
        expected_title = "Student Registration Form"
        actual_title = self.is_element_present(*RegisterPageLocators.TITLE)
        assert expected_title == actual_title.text, "Title was not correct"

    #проверяем наличие формы
    def should_be_user_form(self):
        assert self.wait_for_element(*RegisterPageLocators.USER_FORM), "User form was not found"

    #проверяем наличие всех элементов формы
    def should_be_login_form(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME), "First name field is missing"
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME)
        assert self.is_element_present(*RegisterPageLocators.EMAIL), "Email field is missing"
        assert self.is_element_present(*RegisterPageLocators.GENDER), "Gender field is missing"
        assert self.is_element_present(*RegisterPageLocators.MOBILE_NUMBER), "Mobile number field is missing"
        assert self.is_element_present(*RegisterPageLocators.DATE_OF_BIRTH), "Date of birth field is missing"
        assert self.is_element_present(*RegisterPageLocators.SUBJECTS), "Subjects field is missing"
        assert self.is_element_present(*RegisterPageLocators.HOBBIES), "Hobbies field is missing"
        assert self.is_element_present(*RegisterPageLocators.PICTURE), "Picture field is missing"
        assert self.is_element_present(*RegisterPageLocators.CURRENT_ADDRESS), "Current adress field is missing"
        assert self.is_element_present(*RegisterPageLocators.STATE), "State field is missing"
        assert self.is_element_present(*RegisterPageLocators.CITY), "City is missing"
        assert self.is_element_present(*RegisterPageLocators.SUBMIT_BUTTON), "Submit button is missing"

    #заполяем всю форму валидными данными
    def valid_registration(self):
        pass

    #оставляем обязательные поля пустыми
    def empty_fields(self):
        pass

    #заполняем обязательные поля пробелами
    def fields_filled_with_spaces(self):
        pass

    #заполняем необязательные поля  валидно
    def valid_optional_fields(self):
        pass










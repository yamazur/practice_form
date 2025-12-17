from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import RegisterPageLocators


class RegisterPage(BasePage):

    #проверяем, что заголовок страницы (title) соответствует ожидаемому значению
    def should_be_correct_title(self):
        expected_title = "Student Registration Form"
        actual_title = self.is_element_present(*RegisterPageLocators.TITLE)
        assert expected_title == actual_title.text, "Title was not correct"

    #проверяем наличие формы
    def should_be_user_form(self):
        assert self.wait_for_element(*RegisterPageLocators.USER_FORM), "User form was not found"

    #проверяем наличие всех элементов формы
    def should_be_login_form(self):
        #проверка основных полей ввода
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME), "First name field is missing"
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME), "Last name field is missing"
        assert self.is_element_present(*RegisterPageLocators.EMAIL), "Email field is missing"
        assert self.is_element_present(*RegisterPageLocators.MOBILE_NUMBER), "Mobile number field is missing"
        assert self.is_element_present(*RegisterPageLocators.DATE_OF_BIRTH), "Date of birth field is missing"
        assert self.is_element_present(*RegisterPageLocators.SUBJECTS), "Subjects field is missing"
        assert self.is_element_present(*RegisterPageLocators.CURRENT_ADDRESS), "Current address field is missing"
        assert self.is_element_present(*RegisterPageLocators.PICTURE), "Picture upload field is missing"

        #проверка радио-кнопок Gender
        assert self.is_element_present(*RegisterPageLocators.GENDER_MALE), "Gender Male radio button is missing"
        assert self.is_element_present(*RegisterPageLocators.GENDER_FEMALE), "Gender Female radio button is missing"
        assert self.is_element_present(*RegisterPageLocators.GENDER_OTHER), "Gender Other radio button is missing"

        #проверка лейблов Gender
        assert self.is_element_present(*RegisterPageLocators.GENDER_LABEL_MALE), "Gender Male label is missing"
        assert self.is_element_present(*RegisterPageLocators.GENDER_LABEL_FEMALE), "Gender Female label is missing"
        assert self.is_element_present(*RegisterPageLocators.GENDER_LABEL_OTHER), "Gender Other label is missing"

        #проверка чекбоксов Hobbies
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_SPORTS), "Hobbies Sports checkbox is missing"
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_READING), "Hobbies Reading checkbox is missing"
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_MUSIC), "Hobbies Music checkbox is missing"

        #проверка лейблов Hobbies
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_LABEL_SPORTS), "Hobbies Sports label is missing"
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_LABEL_READING), "Hobbies Reading label is missing"
        assert self.is_element_present(*RegisterPageLocators.HOBBIES_LABEL_MUSIC), "Hobbies Music label is missing"

        #проверка выпадающих списков State & City
        assert self.is_element_present(*RegisterPageLocators.STATE_DROPDOWN), "State dropdown container is missing"
        assert self.is_element_present(*RegisterPageLocators.STATE_INPUT), "State input field is missing"
        assert self.is_element_present(*RegisterPageLocators.CITY_DROPDOWN), "City dropdown container is missing"
        assert self.is_element_present(*RegisterPageLocators.CITY_INPUT), "City input field is missing"

        #проверка кнопки отправки
        assert self.is_element_present(*RegisterPageLocators.SUBMIT_BUTTON), "Submit button is missing"

        #проверка лейблов (текстовых меток)
        assert self.is_element_present(*RegisterPageLocators.LABEL_NAME), "Name label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_EMAIL), "Email label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_MOBILE), "Mobile label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_DATE), "Date of birth label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_SUBJECTS), "Subjects label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_ADDRESS), "Address label is missing"
        assert self.is_element_present(*RegisterPageLocators.LABEL_STATE_CITY), "State and City label is missing"


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










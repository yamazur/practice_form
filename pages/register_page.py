from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):

    # проверка заголовка
    def should_be_correct_title(self):
        expected_title = "Practice Form"
        actual_title = self.wait_for_element(RegisterPageLocators.TITLE).text
        assert actual_title == expected_title, \
            f"Заголовок формы некорректен. Ожидалось: '{expected_title}', Получено: '{actual_title}'"

    # ждем появления элементов
    def should_be_elements_present(self, *locators):
        for locator in locators:
            element = self.wait_for_element(locator)
            assert element is not None, f"Element {locator} is missing"

    # проверка всех элементов формы
    def should_be_elements_in_login_form(self):
        #ждем появление формы
        self.wait_for_element(RegisterPageLocators.USER_FORM)

        # основные поля ввода
        self.should_be_elements_present(
            RegisterPageLocators.FIRST_NAME,
            RegisterPageLocators.LAST_NAME,
            RegisterPageLocators.EMAIL,
            RegisterPageLocators.MOBILE_NUMBER,
            RegisterPageLocators.DATE_OF_BIRTH,
            RegisterPageLocators.SUBJECTS,
            RegisterPageLocators.CURRENT_ADDRESS,
            RegisterPageLocators.PICTURE
        )

        #гендер
        self.should_be_elements_present(
            RegisterPageLocators.GENDER,
        )

        #хобби
        self.should_be_elements_present(
            RegisterPageLocators.HOBBIES,
        )

        # State & City
        self.should_be_elements_present(
            RegisterPageLocators.STATE_DROPDOWN,
            RegisterPageLocators.STATE_INPUT,
            RegisterPageLocators.CITY_DROPDOWN,
            RegisterPageLocators.CITY_INPUT
        )

        # кнопка отправки
        self.should_be_elements_present(RegisterPageLocators.SUBMIT_BUTTON)

        # лейблы формы
        self.should_be_elements_present(
            RegisterPageLocators.LABEL_NAME,
            RegisterPageLocators.LABEL_EMAIL,
            RegisterPageLocators.LABEL_MOBILE,
            RegisterPageLocators.LABEL_DATE,
            RegisterPageLocators.LABEL_SUBJECTS,
            RegisterPageLocators.LABEL_ADDRESS,
            RegisterPageLocators.LABEL_STATE_CITY
        )


    # # заполяем всю форму валидными данными
    # def valid_registration(self):
    #     #заполняем обязательные поля
    #     first_name_input =
    #     last_name_input =
    #     gender_radio_button =
    #     mobile_number_input=
    #
    #     #заполняем необязательные поля
    #     email_input=


    # оставляем обязательные поля пустыми
    def empty_fields(self):
        pass

    # заполняем обязательные поля пробелами
    def fields_filled_with_spaces(self):
        pass

    # заполняем необязательные поля  валидно
    def valid_optional_fields(self):
        pass










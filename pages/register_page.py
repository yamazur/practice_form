from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .locators import RegisterPageLocators
from faker import Faker

class RegisterPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.entered_data = {}

    #корректное отображение страницы регистрации
    def should_be_registration_page(self):
        self.should_be_correct_url()
        self.should_be_correct_title()
        self.should_be_elements_present()
        self.should_be_elements_in_login_form()

    # проверка заголовка
    def should_be_correct_title(self):
        expected_title = "Practice Form"
        actual_title = self.wait_for_element(RegisterPageLocators.TITLE).text
        assert actual_title == expected_title, \
            f"Заголовок формы некорректен. Ожидалось: '{expected_title}', Получено: '{actual_title}'"

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
            RegisterPageLocators.GENDER_LABEL_MALE,
            RegisterPageLocators.GENDER_LABEL_FEMALE,
            RegisterPageLocators.GENDER_LABEL_OTHER,
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

    #взаимодействие с календарем
    def select_date_of_birth(self, day, month, year):
        #кликаем на календарь
        date_of_birth = self.browser.find_element(*RegisterPageLocators.DATE_OF_BIRTH)
        date_of_birth.click()

        #выбираем год
        year_select = Select(self.browser.find_element(*RegisterPageLocators.YEAR_OF_BIRTH))
        year_select.select_by_value(str(year))

        #выбираем месяц
        month_select = Select(self.browser.find_element(*RegisterPageLocators.MONTH_OF_BIRTH))
        month_select.select_by_value(str(month))

        #выбираем день(исключаем дни из соседних месяцев)
        day_elem = self.browser.find_element(
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') "
            f"and not(contains(@class,'--outside-month')) and text()='{day}']"
        )
        day_elem.click()

    # заполяем все поля валидно
    def valid_required_fields(self):

        fake = Faker()

        #заполняем обязательные поля
        #имя
        first_name_input = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name_input.clear()
        first_name = fake.first_name()
        first_name_input.send_keys(first_name)

        #фамилия
        last_name_input = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        last_name_input.clear()
        last_name = fake.last_name()
        last_name_input.send_keys(last_name)

        #гендер
        gender = "Male"
        gender_radio_button = self.browser.find_element(*RegisterPageLocators.GENDER_LABEL_MALE)
        gender_radio_button.click()

        #мобильный телефон
        mobile = "1234567890"
        mobile_number_input = self.browser.find_element(*RegisterPageLocators.MOBILE_NUMBER)
        mobile_number_input.clear()
        mobile_number_input.send_keys(mobile)

        self.entered_data["Student Name"] = f"{first_name} {last_name}"
        self.entered_data["Gender"] = gender
        self.entered_data["Mobile"] = mobile

    def valid_optional_fields(self):

        fake = Faker()

        # почта
        email_input = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_input.clear()
        email = fake.email()
        email_input.send_keys(email)

        #др
        fake_date = fake.date_of_birth(minimum_age=18, maximum_age=60)
        day = fake_date.day
        month = fake_date.month - 1  # для селектора React Datepicker (0 = January)
        year = fake_date.year
        self.select_date_of_birth(day, month, year)
        dob = fake_date.strftime("%d %B,%Y")

        #предмет
        subjects_input = self.browser.find_element(*RegisterPageLocators.SUBJECTS)
        subjects_input.send_keys("Eng")
        english_option = self.browser.find_element(*RegisterPageLocators.ENGLISH_OPTION)
        english_option.click()

        #хобби
        hobbies_checkbox = self.browser.find_element(*RegisterPageLocators.HOBBIES_LABEL_SPORTS)
        hobbies_checkbox.click()

        #фото
        file_path = self.create_test_picture()
        picture_upload = self.browser.find_element(*RegisterPageLocators.PICTURE)
        picture_upload.send_keys(file_path)

        #текущий адрес
        address = fake.address()
        current_address_input = self.browser.find_element(*RegisterPageLocators.CURRENT_ADDRESS)
        current_address_input.clear()
        current_address_input.send_keys(address)

        #штат
        state_dropdown = self.browser.find_element(*RegisterPageLocators.STATE_DROPDOWN)
        state_dropdown.click()
        ncr_option = self.browser.find_element(*RegisterPageLocators.NCR_OPTION)
        ncr_option.click()

        #город
        city_dropdown = self.browser.find_element(*RegisterPageLocators.CITY_DROPDOWN)
        city_dropdown.click()
        delhi_option = self.browser.find_element(*RegisterPageLocators.DELHI_OPTION)
        delhi_option.click()

        #сохраняем данные в словарь entered_data
        self.entered_data["Student Email"] = email
        self.entered_data["Date of Birth"] = dob
        self.entered_data["Subjects"] = "English"
        self.entered_data["Hobbies"] = "Sports"
        self.entered_data["Picture"] = file_path.split("/")[-1]
        self.entered_data["Address"] = address.replace("\n", " ")
        self.entered_data["State and City"] = "NCR Delhi"

    # заполняем обязательные поля пробелами
    def fields_filled_with_spaces(self):
        #имя
        first_name_input = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        first_name_input.clear()
        first_name_input.send_keys(" ")

        #фамилия
        last_name_input = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        last_name_input.clear()
        last_name_input.send_keys(" ")

        #гендер
        gender_radio_button = self.browser.find_element(*RegisterPageLocators.GENDER_LABEL_MALE)
        gender_radio_button.click()

        #мобильный телефон
        mobile_number_input = self.browser.find_element(*RegisterPageLocators.MOBILE_NUMBER)
        mobile_number_input.clear()
        mobile_number_input.send_keys("          ")

    # нажимаем на кнопку submit
    def click_submit_button(self):
        submit_button = self.browser.find_element(*RegisterPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    #проверяем наличие модального окна
    def should_be_success_message(self):
        self.browser.find_element(*RegisterPageLocators.MODAL_WINDOW)

    #проверяем данные в модальном окне
    def should_be_correct_success_message(self):
        #находим все строки таблицы в модальном окне
        rows = self.browser.find_elements(*RegisterPageLocators.MODAL_ROWS)

        #создаём словарь для данных из модального окна
        modal_data = {}

        #проходим по каждой строке таблицы
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")  # получаем все ячейки строки
            key = cells[0].text.strip()  # первая ячейка - ключ (название поля)
            value = cells[1].text.strip()  # вторая ячейка - значение
            if key:
                modal_data[key] = value

        #проверяем, что данные совпадают с введёнными
        assert modal_data == self.entered_data, (
            f"Данные в модальном окне не совпадают.\n"
            f"Ожидалось: {self.entered_data}\n"
            f"Получено: {modal_data}"
        )

    #проверка на то, что сообщение об успехе отсутствует
    def should_not_be_success_message(self):
        """Проверяет, что нет сообщения об успехе"""
        assert self.is_not_element_present(RegisterPageLocators.MODAL_WINDOW),  \
            "Success message is presented, but should not be"


















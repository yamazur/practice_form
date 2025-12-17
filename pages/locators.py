from selenium.webdriver.common.by import By

class RegisterPageLocators:

    TITLE = (By.CSS_SELECTOR, "h5.text-center")
    USER_FORM = (By.ID, "userForm")

    #основные поля ввода
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE_NUMBER = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PICTURE = (By.ID, "uploadPicture")

    #радио-кнопки (Gender)
    GENDER_MALE = (By.ID, "gender-radio-1")
    GENDER_FEMALE = (By.ID, "gender-radio-2")
    GENDER_OTHER = (By.ID, "gender-radio-3")
    GENDER_LABEL_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_LABEL_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_LABEL_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    #чекбоксы (Hobbies)
    HOBBIES_SPORTS = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC = (By.ID, "hobbies-checkbox-3")
    HOBBIES_LABEL_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_LABEL_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_LABEL_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")

    #выпадающие списки (State & City)
    STATE_DROPDOWN = (By.ID, "state")  # контейнер
    STATE_INPUT = (By.ID, "react-select-3-input")  #поле ввода
    STATE_OPTIONS = (By.CSS_SELECTOR, "#state .css-26l3qy-menu")

    CITY_DROPDOWN = (By.ID, "city")  # контейнер
    CITY_INPUT = (By.ID, "react-select-4-input")  #поле ввода
    CITY_OPTIONS = (By.CSS_SELECTOR, "#city .css-26l3qy-menu") #выпадающее меню

    #кнопка отправки
    SUBMIT_BUTTON = (By.ID, "submit")

    #лейблы
    LABEL_NAME = (By.ID, "userName-label")
    LABEL_EMAIL = (By.ID, "userEmail-label")
    LABEL_MOBILE = (By.ID, "userNumber-label")
    LABEL_DATE = (By.ID, "dateOfBirth-label")
    LABEL_SUBJECTS = (By.ID, "subjects-label")
    LABEL_ADDRESS = (By.ID, "currentAddress-label")
    LABEL_STATE_CITY = (By.ID, "stateCity-label")

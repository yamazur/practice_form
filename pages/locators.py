from selenium.webdriver.common.by import By

class RegisterPageLocators:

    TITLE = (By.CSS_SELECTOR, "h1.text-center")
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

    #гендер
    GENDER = (By.ID, "genterWrapper")

    #хобби
    HOBBIES = (By.ID, "hobbiesWrapper")

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

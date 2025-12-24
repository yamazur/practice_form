from selenium.webdriver.common.by import By

class RegisterPageLocators:

    TITLE = (By.CSS_SELECTOR, "h1.text-center")
    USER_FORM = (By.ID, "userForm")

    #основные поля ввода
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE_NUMBER = (By.ID, "userNumber")
    SUBJECTS = (By.ID, "subjectsInput")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PICTURE = (By.ID, "uploadPicture")

    #гендер
    GENDER = (By.ID, "genterWrapper")
    GENDER_LABEL_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_LABEL_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_LABEL_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")

    #хобби
    HOBBIES = (By.ID, "hobbiesWrapper")
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

    #значения в выпадающих списках
    ENGLISH_OPTION = (By.XPATH, "//div[contains(@class, 'option') and text()='English']")
    NCR_OPTION = (By.XPATH, "//div[contains(@class,'option') and text()='NCR']")
    DELHI_OPTION = (By.XPATH, "//div[contains(@class,'option') and text()='Delhi']")

    #модальное окно
    MODAL_WINDOW = (By.CSS_SELECTOR, ".modal-content")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    MODAL_ROWS = (By.CSS_SELECTOR, ".table-responsive tbody tr")
    MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")

    #календарь
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DAY_OF_BIRTH = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'--outside-month')) and text()='18']")

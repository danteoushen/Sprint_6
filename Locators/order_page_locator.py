from selenium.webdriver.common.by import By

class OrderPageLocator:
    #Форма для кого самокат
    FOR_WHO_LOCATOR = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    # Локаторы для ввода для кого самокат
    NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Адрес: куда привезти заказ')]")
    SUBWAY_FIELD = (By.XPATH, ".//input[contains(@placeholder,'Станция метро')]")
    SELECT_METRO = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_NUMBER = (By.XPATH, ".//input[contains(@placeholder,'Телефон: на него позвонит курьер')]")

    #Кнопка Далее
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    #Форма про аренду
    ABOUT_RENT_LOCATOR = (By.XPATH, "//div[text()='Про аренду']")

    # Локаторы для ввода про аренду
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CHOOSE_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    PERIOD_LIST = (By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'сутки')]")
    COLOR = (By.XPATH, "//input[@id='grey']")
    COMMENT = (By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]")

    #Кнопка заказать
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']")

    #Кнопка Да в всплывающем окне
    ACCEPT_ORDER = (By.XPATH, ".//button[text()='Да']")
    #Текст заказ оформлен
    CHECK_STATUS = (By.XPATH, "//div[text()='Заказ оформлен']")
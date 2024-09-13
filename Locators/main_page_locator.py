from selenium.webdriver.common.by import By

class MainPageLocator:

    #Кнопка заказать в шапке страницы
    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    # Кнопка заказать в середине страницы
    DOWN_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")

    #Кнопка Яндекса в шапке страницы
    YANDEX_BUTTON = (By.XPATH, "//a[@href='//yandex.ru']")
    #Кнопка самоката в шапке страницы
    SAMOKAT_BUTTON = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    #Кнопка принять куки
    COOKIE_ACCEPT_BUTTON = (By.XPATH, ".//button[text()='да все привыкли']")




    #Надпись раздела с вопросами
    FAQ_LOCATOR = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')


    # Кнопка с выпадающим впоросом
    QUESTIONS = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }
    # Поле с ответом на вопрос
    ANSWERS = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }



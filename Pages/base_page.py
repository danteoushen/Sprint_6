import allure
from data.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Ожидание появление элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    #Нажать на элемент
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    #Ввести текст
    def input_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    #Получить текст
    def get_text_on_element(self, locator):
        return self.find_element_with_wait(locator).text

    #Скролл
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    #Переключиться на другую вкладку
    def switch(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    #Ожидание загрузки
    def wait_loading(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    #Получить текущий URL
    def get_url(self):
        return self.driver.current_url




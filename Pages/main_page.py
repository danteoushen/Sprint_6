import allure
from Pages.base_page import BasePage
from Locators.main_page_locator import MainPageLocator

class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Заказать" в хэдере страницы')
    def click_top_order_button(self):
        self.find_element_with_wait(MainPageLocator.HEADER_ORDER_BUTTON).click()

    @allure.step('Кликнуть по кнопке "Заказать" в середине страницы')
    def click_down_order_button(self):
        self.find_element_with_wait(MainPageLocator.DOWN_ORDER_BUTTON).click()

    @allure.step('Кликнуть по лого Яндекса в хэдере страницы')
    def click_yandex_button(self):
        self.find_element_with_wait(MainPageLocator.YANDEX_BUTTON).click()

    @allure.step('Переключиться на другую вкладку')
    def switch_tab_on_browserer(self):
        return self.switch()

    @allure.step('Кликнуть по лого Самоката в хэдере страницы')
    def click_samokat_button(self):
        self.find_element_with_wait(MainPageLocator.SAMOKAT_BUTTON).click()

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocator.FAQ_LOCATOR)

    @allure.step('Ожидание появляения вопросов')
    def wait_visibility_question(self, data):
        self.find_element_with_wait(MainPageLocator.QUESTIONS[data])

    @allure.step('Нажать на вопрос')
    def click_on_question(self, data):
        self.click_to_element(MainPageLocator.QUESTIONS[data])

    @allure.step('Ожидание появляения вопросов')
    def wait_visibility_answer(self, data):
        self.find_element_with_wait(MainPageLocator.ANSWERS[data])

    @allure.step('Получить ответ')
    def get_answer(self, data):
        return self.get_text_on_element(MainPageLocator.ANSWERS[data])


    @allure.step('Приянть куки')
    def click_to_cooke_accept(self):
        self.click_to_element(MainPageLocator.COOKIE_ACCEPT_BUTTON)



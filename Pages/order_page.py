import allure
from Pages.base_page import BasePage
from Locators.order_page_locator import OrderPageLocator
from Locators.main_page_locator import MainPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import OrderData


class OrderPage(BasePage):

    @allure.step('Заполнение формы "Для кого самокат"')
    def data_first_form(self, test_data):
        self.input_text_to_element(OrderPageLocator.NAME_INPUT, test_data[0])
        self.input_text_to_element(OrderPageLocator.LAST_NAME_INPUT, test_data[1])
        self.input_text_to_element(OrderPageLocator.ADDRESS_INPUT, test_data[2])
        self.click_to_element(OrderPageLocator.SUBWAY_FIELD)
        self.input_text_to_element(OrderPageLocator.SUBWAY_FIELD, test_data[3])
        self.click_to_element(OrderPageLocator.SELECT_METRO)
        self.input_text_to_element(OrderPageLocator.PHONE_NUMBER, test_data[4])
        self.click_to_element(MainPageLocator.COOKIE_ACCEPT_BUTTON)
        self.find_element_with_wait(OrderPageLocator.NEXT_BUTTON)
        self.click_to_element(OrderPageLocator.NEXT_BUTTON)



    def data_second_form(self, test_data):
        self.find_element_with_wait(OrderPageLocator.DATE)
        self.click_to_element(OrderPageLocator.DATE)
        self.input_text_to_element(OrderPageLocator.DATE, test_data[5])
        self.click_to_element(OrderPageLocator.COLOR)
        self.click_to_element(OrderPageLocator.PERIOD_FIELD)
        self.click_to_element(OrderPageLocator.PERIOD_LIST)
        self.click_to_element(OrderPageLocator.COMMENT)
        self.input_text_to_element(OrderPageLocator.COMMENT, test_data[6])
        self.click_to_element(OrderPageLocator.ORDER_BUTTON)
        self.find_element_with_wait(OrderPageLocator.ACCEPT_ORDER)
        self.click_to_element(OrderPageLocator.ACCEPT_ORDER)

    def check_order(self):
        return self.get_text_on_element(OrderPageLocator.CHECK_STATUS)













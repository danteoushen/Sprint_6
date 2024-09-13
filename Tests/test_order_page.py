import allure
from conftest import driver
from Pages.order_page import OrderPage
from Locators.main_page_locator import MainPageLocator
from data.test_data import OrderData
import pytest

class TestOrderScooter:
    @allure.title('Проверка создания заказа через кнопку вверху страницы и в середине, с двумя наборами данных')

    @pytest.mark.parametrize('button, test_data', [(MainPageLocator.HEADER_ORDER_BUTTON, OrderData.test_user1),
                                               (MainPageLocator.DOWN_ORDER_BUTTON, OrderData.test_user2)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.find_element_with_wait(button)
        order_page.click_to_element(button)
        order_page.data_first_form(test_data)
        order_page.data_second_form(test_data)
        assert 'Заказ оформлен' in order_page.check_order()

import allure
import pytest
from Pages.main_page import MainPage
from conftest import driver
from data.test_data import HomePageFAQ
from data.urls import Urls


class TestQuestionOnPage:

    @allure.title('Раздел "Вопросы о важном"')
    @allure.description('Проверка вопросов и ответов')
    @pytest.mark.parametrize('question_number, expected_answer', HomePageFAQ.test_data_faq)
    def test_click_faq(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_question(question_number)
        main_page.click_on_question(question_number)
        main_page.wait_visibility_answer(question_number)
        assert main_page.get_answer(question_number) == expected_answer

class TestRedirect:
    @allure.title('Проверка перехода при клике на лого Яндекса')
    def test_logo_redirect_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_button()
        main_page.switch_tab_on_browserer()
        main_page.wait_loading(Urls.DZEN_HOME_PAGE)
        assert main_page.get_url() == Urls.DZEN_HOME_PAGE

    @allure.title('Проверка перехода при клике на лого Самоката')
    def test_logo_redirect_samokat(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_order_button()
        main_page.click_samokat_button()
        assert main_page.get_url() == Urls.BASE_PAGE


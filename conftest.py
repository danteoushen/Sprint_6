import pytest
from selenium import webdriver
from data.urls import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_PAGE)
    yield driver
    driver.quit()
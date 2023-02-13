from pages.text_box_page import TextBox
import time
import allure
from selenium.webdriver.common.keys import Keys

@allure.feature('check attr')
@allure.story('Проверка значения атрибута элемента')
@allure.severity(allure.severity_level.NORMAL)
def test_text_box(browser):
    '''проверка значения атрибута элемента'''
    text_box_page = TextBox(browser)
    text_box_page.visit()

    text_box_page.visit()
    assert text_box_page.full_name.exist()

    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'

@allure.feature('check attr')
@allure.story('Проверка наличия атрибута')
@allure.severity(allure.severity_level.CRITICAL)
def test_attr_exist(browser):
    '''проверка наличия атрибута'''
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.btn_first.click()
    time.sleep(2)

    assert text_box_page.box_first_menu.get_dom_attribute('style')

@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)
def test_attr_not_exist(browser):
    '''проверка отсутствия атрибута'''
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert not text_box_page.btn_first.get_dom_attribute('style')
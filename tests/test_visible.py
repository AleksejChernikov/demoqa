from pages.elements_page import ElementsPage
from pages.accordian_page import AccordianPage
import time


def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    #elements_page.btn_sidebar_first.click()
    time.sleep(3)
    assert elements_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert elements_page.btn_sidebar_first_checkbox.not_visible()

def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.one_paragraph.visible()
    accordian_page.one_section_btn.click()
    time.sleep(2)
    assert accordian_page.one_paragraph.not_visible()

def test_visible_default_accordian(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.one_paragraph.visible()
    accordian_page.one_section_btn.click()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    assert accordian_page.one_paragraph.not_visible()
    browser.refresh()
    browser.set_window_size(1000, 1000)
    assert accordian_page.one_paragraph.visible()


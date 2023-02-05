from pages.modal_dialogs_page import Modal_dialogsPage
from pages.elements_page import ElementsPage


def test_elements_dz(browser):
    elements_dz_page = Modal_dialogsPage(browser)
    elements_dz_page.visit()
    assert elements_dz_page.btns_third_menu.check_count_elements(5)

def test_navigation_dz(browser):
    elements_dz_page = Modal_dialogsPage(browser)
    elements_dz_page.visit()
    browser.refresh()
    elements_dz_page.btn_alerts.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()



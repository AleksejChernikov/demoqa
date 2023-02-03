from pages.modal_dialogs_page import Modal_dialogsPage

def test_elements_dz(browser):
    elements_dz_page = Modal_dialogsPage(browser)
    elements_dz_page.visit()
    assert elements_dz_page.btns_third_menu.check_count_elements(5)
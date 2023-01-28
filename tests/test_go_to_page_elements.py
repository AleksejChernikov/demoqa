from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    qaz = Demoqa(browser)
    qaz2 = ElementsPage(browser)
    qaz.visit()
    assert qaz.equal_url()
    qaz.btn_elements.click()
    assert qaz2.equal_url()
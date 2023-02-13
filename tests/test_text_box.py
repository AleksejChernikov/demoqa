from pages.text_box_page import TextBox
import time
from selenium.webdriver.common.keys import Keys

def test_text_box(browser):

    text_box_page = TextBox(browser)

    test_text_name = 'tester testerovich'
    test_text_address = 'Moskow, Krasnaya Ploshad, 1'

    text_box_page.visit()
    time.sleep(10)
    text_box_page.full_name.send_keys(test_text_name)
    text_box_page.current_address.send_keys(test_text_address)
    time.sleep(2)
    text_box_page.submit.click_force()
    time.sleep(2)

    assert text_box_page.proverka_name.get_text() == 'Name:' + test_text_name
    assert text_box_page.proverka_address.get_text() == 'Current Address :' + test_text_address
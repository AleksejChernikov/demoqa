from pages.text_box_page import TextBox
import time
from selenium.webdriver.common.keys import Keys

def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    text_box_page.full_name.send_keys('Alex')
    time.sleep(2)
    text_box_page.full_name.clear()
    time.sleep(2)

    assert text_box_page.full_name.get_text() == ''
from pages.text_box_page import TextBox
import time
from selenium.webdriver.common.keys import Keys

def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('tester testerovich')
    time.sleep(2)
    text_box_page.current_address.send_keys('Moskow, Krasnaya Ploshad, 1')
    time.sleep(2)
    text_box_page.submit.click()
    time.sleep(3)


from pages.base_page import BasePage
from components.components import WebElement

class Modal_dialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
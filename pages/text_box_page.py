from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit = WebElement(driver, '#submit')

        self.box_first_menu = WebElement(driver, locator='div.row > div:nth-child(1) > div > div > div:nth-child(1) > div')
        self.btn_first = WebElement(driver, locator='div > div > div:nth-child(1) > span')

        self.proverka_name = WebElement(driver, '#name')
        self.proverka_address = WebElement(driver, 'p#currentAddress')

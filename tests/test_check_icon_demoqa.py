from pages.demoqa import Demoqa

def test_icon_exist(browser):
    # browser.get('https://demoqa.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')
    qaz = Demoqa(browser)
    qaz.visit()
    qaz.icon.click()
    assert qaz.equal_url()
    assert qaz.exist_icon()
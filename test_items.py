import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_bucket_button(browser):
    browser.get(link)
    time.sleep(10)

    button = browser.find_element_by_xpath("//form[@class='add-to-basket']//button")
    assert button.is_displayed(), 'Not Visible'


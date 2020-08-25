import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_in_different_languages(browser):
    browser.get(link)
    #time.sleep(5)
    # you can try to use: pytest --language=es test_items.py
    # or: pytest -s -v --language=fr test_items.py
    button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    #or assert True
    assert button, "Oops, we can't find button"
    #убеждаемся, что кнопку действительно нашли. без ручной проверки time.sleep()
    print('\n' + button.text)
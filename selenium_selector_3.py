from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get( link )

    text_elements = browser.find_elements_by_css_selector( '[type="text"]' )
    for element in text_elements :
        element.send_keys( "My answer" )

    button = browser.find_elements_by_css_selector( 'button.btn' )
    button.click()

finally:
    time.sleep(30)
    browser.quit()
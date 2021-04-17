from selenium import webdriver
import time
import math

def calc( num1 ):
    x = int( num1 )
    return str( math.log( abs( 12*math.sin( int( x ) ) ) ) )

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get( link )
    button = browser.find_element_by_css_selector( 'button.btn' )
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num1 = browser.find_element_by_id( 'input_value' ).text
    input_answer = browser.find_element_by_id( 'answer' )
    input_answer.send_keys( calc( num1 ) )

    button_submit = browser.find_element_by_css_selector( 'button.btn' )
    button_submit.click()


finally:
    time.sleep( 10 )
    browser.quit()


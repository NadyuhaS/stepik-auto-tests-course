from selenium import webdriver
import time
import math

def calc( num1 ):
    x = int( num1 )
    return str( math.log( abs( 12*math.sin( int( x ) ) ) ) )

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get( link )
    button = browser.find_element_by_css_selector( 'button.btn' )
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window( new_window )
    num1 = browser.find_element_by_css_selector( '#input_value' ).text
    answer = browser.find_element_by_css_selector( '#answer' )
    answer.send_keys( calc( num1 ) )

    button_submit = browser.find_element_by_css_selector( 'button.btn' )
    button_submit.click()


finally:
    time.sleep( 10 )
    browser.quit()
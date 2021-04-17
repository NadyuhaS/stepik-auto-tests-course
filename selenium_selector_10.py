from selenium import webdriver
import os
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get( link )

    input_name = browser.find_element_by_name( 'firstname' )
    input_name.send_keys('Nad')
    input_surname = browser.find_element_by_name( 'lastname' )
    input_surname.send_keys( 'nice' )
    input_email = browser.find_element_by_name( 'email' )
    input_email.send_keys('num@num.com')

    current_dir = os.path.abspath( os.path.dirname(__file__) )
    file_path = os.path.join( current_dir, 'file.txt' )

    file = browser.find_element_by_name( 'file' )
    file.send_keys( file_path )

    button = browser.find_element_by_css_selector( 'button.btn' )
    button.click()

finally:
    time.sleep( 10 )
    browser.quit()

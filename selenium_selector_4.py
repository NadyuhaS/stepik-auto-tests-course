from selenium import webdriver
import  time
import math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get( link )

    input1 = browser.find_element_by_name( "first_name" )
    input1.send_keys( "Nadya" )
    input2 = browser.find_element_by_name( "last_name" )
    input2.send_keys( "Star" )
    input3 = browser.find_element_by_class_name( "city" )
    input3.send_keys( "spbb" )
    input4 = browser.find_element_by_id( "country" )
    input4.send_keys( "SPB" )

    #button = browser.find_elements_by_css_selector( "button.btn" )
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep( 30 )
    browser.quit()

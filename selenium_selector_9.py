from selenium import webdriver
import math
import time
import string
from selenium.webdriver.support.ui import Select

def calc( num1 ) :
    x = int( num1 )
    return str( math.log(abs(12*math.sin(int(x)))) )


link = "http://suninjuly.github.io/execute_script.html"
try :
    browser = webdriver.Chrome()
    browser.get( link )

    num1 = browser.find_element_by_id( 'input_value' ).text
    input1 = browser.find_element_by_id('answer')
    browser.execute_script( "return arguments[0].scrollIntoView( true );", input1 )
    input1.send_keys( calc( num1 ) )

    browser.execute_script("window.scrollBy(0, 200);")

    checkBox = browser.find_element_by_id( 'robotCheckbox' )
    checkBox.click()

    radioBox = browser.find_element_by_id( 'robotsRule' )
    radioBox.click()

    button = browser.find_element_by_css_selector( 'button.btn' )
    button.click()

finally :
    time.sleep( 10 )
    browser.quit()
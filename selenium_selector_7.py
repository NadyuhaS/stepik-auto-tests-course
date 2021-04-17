from selenium import webdriver
import time
import math
import string

def calculate_answer(  value ) :
    x = int( value )
    answer = math.log(abs(12*math.sin(int(x))))

    return str( answer )


link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get( link )
    expression_question = browser.find_element_by_css_selector('img#treasure')
    x_value = expression_question.get_attribute( 'valuex' )


    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys( calculate_answer(  x_value ) )

    checkBox = browser.find_element_by_css_selector('#robotCheckbox')
    checkBox.click()

    radioButton = browser.find_element_by_css_selector('#robotsRule')
    radioButton.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep( 10 )
    browser.quit()
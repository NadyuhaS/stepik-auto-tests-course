from selenium import webdriver
import math
import time
import string
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
try :
    browser = webdriver.Chrome()
    browser.get( link )

    num1 = browser.find_element_by_id( 'num1' ).text
    num2 = browser.find_element_by_id( 'num2' ).text

    select = Select( browser.find_element_by_tag_name( 'select' ) )
    select.select_by_value( str( int( num1 ) + int( num2 ) ) )

    button = browser.find_element_by_css_selector( 'button.btn' )
    button.click()

finally :
    time.sleep( 10 )
    browser.quit()
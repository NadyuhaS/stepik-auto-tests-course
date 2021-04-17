from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc( num1 ):
    x = int( num1 )
    return str( math.log( abs( 12*math.sin( int( x ) ) ) ) )


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
text = WebDriverWait( browser, 12 ).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id( 'book' )
button.click()

browser.execute_script("window.scrollBy(0, 500);")

num1 = browser.find_element_by_id( 'input_value' ).text
input_answer = browser.find_element_by_id( 'answer' )
input_answer.send_keys( calc( num1 ) )

button_sub = browser.find_element_by_id( 'solve' )
button_sub.click()

time.sleep(10)
browser.quit()


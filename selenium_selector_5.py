from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[required]')
    input1.send_keys('NAdya')
    input2 = browser.find_element_by_xpath('//input[@class="form-control second" and @required]')
    input2.send_keys('STar')
    input3 = browser.find_element_by_class_name( 'third' )
    input3.send_keys('num@num.com')

    input4 = browser.find_element_by_css_selector('.second_block .first')
    input4.send_keys('12345')
    input5 = browser.find_element_by_css_selector('.second_block .second')
    input5.send_keys('456789')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
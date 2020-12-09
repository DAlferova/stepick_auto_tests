"""
https://stepik.org/lesson/181384/step/8?unit=156009

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и
отправить решение

.text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    #  Нажать на кнопку Book.
    button = browser.find_element_by_tag_name("button")
    button.click()

    #  Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    x = int(x)
    #  Посчитать математическую функцию от x
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(str(y))

    #  Нажать на кнопку Submit.
    button = browser.find_element_by_id("solve")
    # time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # time.sleep(1)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

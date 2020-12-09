"""
https://stepik.org/lesson/228249/step/6?unit=200781
Задание на execute_script:
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    #  Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    x = int(x)
    #  Посчитать математическую функцию от x
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(str(y))
    # time.sleep(1)

    #  Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    # time.sleep(1)

    #  Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    # time.sleep(1)

    #  Нажать на кнопку Submit.
    button = browser.find_element_by_tag_name("button")
    # time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # time.sleep(1)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

"""
https://stepik.org/lesson/184253/step/4?unit=158843
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом

prompt.send_keys("My answer")
confirm.dismiss()
alert_text = alert.text
"""
from selenium import webdriver
import time
import math


def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    #  нажимаем кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()

    #  Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    #  Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    x = int(x)
    #  Посчитать математическую функцию от x
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #  Нажать на кнопку Submit.
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

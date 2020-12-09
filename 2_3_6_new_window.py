"""
https://stepik.org/lesson/184253/step/6?unit=158843
Задание: переход на новую вкладку

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""
from selenium import webdriver
import time
import math


def calc(x_value):
    return str(math.log(abs(12*math.sin(int(x_value)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    #  нажимаем кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()

    #  Выясняем имя новой вкладки и переключаемся на нее
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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

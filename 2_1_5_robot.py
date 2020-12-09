"""
https://stepik.org/lesson/165493/step/5?unit=140087
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

Атрибут text возвращает текст, который находится между открывающим и закрывающим
тегами элемента.
Например, text для данного элемента <div class="message">У вас новое сообщение.</div>
вернёт строку: "У вас новое сообщение".
"""

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #  Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    x = int(x)
    #  Посчитать математическую функцию от x
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    #  Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    #  Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    time.sleep(1)
    #  Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

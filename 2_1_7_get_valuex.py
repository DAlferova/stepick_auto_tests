"""
https://stepik.org/lesson/165493/step/7?unit=140087

# Найти на ней элемент-картинку/
Взять у этого элемента значение атрибута valuex
valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x,
Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!".
Нажать на кнопку Отправить.
for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()
"""
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    #  Считать значение для переменной x
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
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

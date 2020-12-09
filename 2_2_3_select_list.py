"""
https://stepik.org/lesson/228249/step/3?unit=200781

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"

"""

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link2)


try:
    #  Считать значение для переменной num1
    num1 = browser.find_element_by_id("num1")
    num1 = int(num1.text)
    #  Считать значение для переменной num2
    num2 = browser.find_element_by_id("num2")
    num2 = int(num2.text)
    #  Считать значение для переменной action
    # action = browser.find_element_by_css_selector(".nowrap:nth-child(3)")
    # print(action)
    # print(action.text)

    #  Посчитать сумму
    y = num1 + num2

    #  Выбрать ответ из выпадающего списка
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))  # ищем элемент с текстом y

    time.sleep(1)
    #  Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

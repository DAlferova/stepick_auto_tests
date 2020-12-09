"""
https://stepik.org/lesson/228249/step/4?unit=200781
Давайте попробуем вызвать alert в браузере с помощью WebDriver.

Выполнение JavaScript на странице - это неописанный в документации Selenium
способ поиска элемента.
Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
element = browser.execute_script('document.getElementsByName("name")')

Так же есть конструкции:
getElementById
getElementsByTagName
getElementsByClassName
querySelector - для CSS
querySelectorAll - для CSS (находит все совпадения)

evaluate - для XPATH.
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # browser.execute_script("alert('Robots at work');")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

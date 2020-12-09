"""
https://stepik.org/lesson/228249/step/8?unit=200781
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Darya")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("A")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("email")

    #  Присабачить файл.
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла и добавляем наш файл
    file_path = os.path.join(current_dir, 'text_file.txt')
    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path)
    # time.sleep(1)

    #  Нажать на кнопку Submit.
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

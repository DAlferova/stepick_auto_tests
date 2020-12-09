"""
https://stepik.org/lesson/228249/step/5?unit=200781
An example with error and scrolling
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    button = browser.find_element_by_tag_name("button")
    time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(2)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

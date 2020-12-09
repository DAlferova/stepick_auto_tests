"""
https://stepik.org/lesson/181384/step/6?unit=156009
Какую ошибку вы увидите в консоли?
"""
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

try:
    button = browser.find_element_by_id("button")
    # button.click()
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

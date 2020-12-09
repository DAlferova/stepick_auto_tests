"""
https://stepik.org/lesson/181384/step/7?unit=156009
WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной.
На странице мы специально задали программно паузу в 1 секунду после загрузки
сайта перед активированием кнопки, но неактивная кнопка в момент загрузки —
обычное дело для реального сайта.

Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и
дождаться, когда кнопка станет кликабельной. Для реализации подобных ожиданий
в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits),
которые позволяют задать специальное ожидание для конкретного элемента.
Задание явных ожиданий реализуется с помощью инструментов WebDriverWait
и expected_conditions.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element_by_id("verify_message")

    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(
    #         EC.element_to_be_clickable((By.ID, "verify"))
    #     )

    assert "successful" in message.text
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

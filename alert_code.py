from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import unittest, time, re

link = "http://suninjuly.github.io/alert_accept.html"


# Проводим расчет формулы
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    element = WebDriver.find_element_by_tag_name('button')
    element.click()
    # Для переключения на окно confirm используется:
    confirm = WebDriver.switch_to.alert
    # Принимаем
    confirm.accept()
    element_x = WebDriver.find_element_by_id('input_value')
    # Забираем текст, который находится между открывающим и закрывающим тегами элемента
    x = element_x.text
    y = calc(x)
    element1 = WebDriver.find_element_by_id('answer')
    element1.send_keys(y)
    button = WebDriver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

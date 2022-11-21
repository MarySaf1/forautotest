from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    button = WebDriver.find_element_by_tag_name("button")
    button.click()
    new_window = WebDriver.window_handles[1]
    WebDriver.switch_to.window(new_window)
    element_x = WebDriver.find_element_by_id('input_value')
    # Забираем текст, который находится между открывающим и закрывающим тегами элемента
    x = element_x.text
    y = calc(x)
    element1 = WebDriver.find_element_by_id('answer')
    element1.send_keys(y)

    button2 = WebDriver.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

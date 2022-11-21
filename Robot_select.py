from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


# def calc(x, y):
#     return str(math.log(abs(x + y)))


try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    element_x = WebDriver.find_element_by_id('num1')
    x = element_x.text
    element_y = WebDriver.find_element_by_id('num2')
    y = element_y.text
    z = int(x) + int(y)
    str_z = str(z)

    select = Select(WebDriver.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str_z)

    button = WebDriver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

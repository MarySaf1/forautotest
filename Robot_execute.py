from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    element_x = WebDriver.find_element_by_id('input_value')
    x = element_x.text
    y = calc(x)
    element1 = WebDriver.find_element_by_id('answer')
    element1.send_keys(y)
    button = WebDriver.find_element_by_tag_name("button")
    # Скроллим стр вниз,чтобы открыть перекрытый элемент
    WebDriver.execute_script("return arguments[0].scrollIntoView(true);", button)
    element1 = WebDriver.find_element_by_id('answer')
    element1.send_keys(y)
    option1 = WebDriver.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = WebDriver.find_element_by_id('robotsRule')
    option2.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)
    # говорим WebDriver ждать, когда цена дома уменьшится до $100
    find_price = WebDriverWait(WebDriver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = WebDriver.find_element(By.ID, value='book')
    button.click()
    element_x = WebDriver.find_element_by_id('input_value')
    # Забираем текст, который находится между открывающим и закрывающим тегами элемента
    x = element_x.text
    y = calc(x)
    element1 = WebDriver.find_element_by_id('answer')
    element1.send_keys(y)

    button2 = WebDriver.find_element(By.ID, value='solve')
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()


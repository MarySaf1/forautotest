import os
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    input1 = WebDriver.find_element(by=By.NAME, value='firstname')
    input1.send_keys("Ivan")
    input2 = WebDriver.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = WebDriver.find_element_by_name('email')
    input3.send_keys("fdf@fr.ru")
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    button_file = WebDriver.find_element_by_id('file')
    # отправляем файл
    button_file.send_keys(file_path)
    button = WebDriver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

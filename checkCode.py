from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    element1 = WebDriver.find_element_by_css_selector("input.form-control.first")
    element1.send_keys("Privet")
    element2 = WebDriver.find_element_by_css_selector("input.form-control.second")
    element2.send_keys("Privet")
    element3 = WebDriver.find_element_by_css_selector("input.form-control.third")
    element3.send_keys("Privet")

    # Отправляем заполненную форму
    button = WebDriver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = WebDriver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input[type=text]")
    for element in elements:
        element.send_keys("Privet")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

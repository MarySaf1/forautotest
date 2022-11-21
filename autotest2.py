# -*- coding: utf-8 -*-
import random, time, queue
import math
import multiprocessing

multiprocessing.set_start_method('spawn')
import psutil

psutil.getloadavg()

from multiprocessing.managers import BaseManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

link = "http://suninjuly.github.io/find_link_text"


try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.get(link)

    input0 = WebDriver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    input0.click()
    input1 = WebDriver.find_element(by=By.NAME, value='first_name')
    input1.send_keys("Ivan")
    input2 = WebDriver.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = WebDriver.find_element_by_name('firstname')
    input3.send_keys("Smolensk")
    input4 = WebDriver.find_element_by_id('country')
    input4.send_keys("Russia")
    button = WebDriver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()

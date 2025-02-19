from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from faker import Faker
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(2)
    # browser.find_element(By.TAG_NAME, "select").click()
    # time.sleep(3)
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # browser.find_element(By.CSS_SELECTOR, "[value='2']").click()

    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value("1") # ищем элемент с текстом "Python"  поиск по значению атрибута value
    # select.select_by_visible_text("2") # ищем элемент с текстом выбора
    # select.select_by_index(index)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(int(num1)+int(num2)))
    browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
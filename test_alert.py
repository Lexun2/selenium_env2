from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os
from faker import Faker
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button_alert = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_alert.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()

    input_value = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text

    input_answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input_answer.send_keys(calc(input_value))

    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()

   

    # как можно создать файл в питоне
    # with open("test.txt", "w") as file:
    #   content = file.write("automationbypython")  # create test.txt file
    #   file.write("123")

    # input1 = browser.find_element(By.CSS_SELECTOR,"#input_value").text
    # answer = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
    # answer.send_keys(calc(input1))
    # browser.find_element(By.CSS_SELECTOR,"input[type='checkbox'][id='robotCheckbox']").click()
    # robotsRule = browser.find_element(By.ID,"robotsRule")
    # _ = robotsRule.location_once_scrolled_into_view
    # robotsRule.click()
    # #browser.find_element(By.CSS_SELECTOR,"input[type='radio'][id='robotsRule']").click()
    # button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
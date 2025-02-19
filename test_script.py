from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from faker import Faker
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR,"#input_value").text
    answer = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
    answer.send_keys(calc(input1))
    browser.find_element(By.CSS_SELECTOR,"input[type='checkbox'][id='robotCheckbox']").click()
    robotsRule = browser.find_element(By.ID,"robotsRule")
    _ = robotsRule.location_once_scrolled_into_view
    robotsRule.click()
    #browser.find_element(By.CSS_SELECTOR,"input[type='radio'][id='robotsRule']").click()
    button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
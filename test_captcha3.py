from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from faker import Faker

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR,"#treasure").get_attribute("valuex")
    answer = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
    answer.send_keys(calc(input1))
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,"input[type='checkbox'][id='robotCheckbox']").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,"input[type='radio'][id='robotsRule']").click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
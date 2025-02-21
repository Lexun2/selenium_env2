from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from faker import Faker
from Bibliotiki import *

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_captcha():
    try: 
        link = "https://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR,"span[id='input_value']")
        A = input1.text
        print(A)
        time.sleep(1)
        answer = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
        answer.send_keys(calc(A))
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input[type='checkbox'][id='robotCheckbox']").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input[type='radio'][id='robotsRule']").click()
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
        button.click()
        try:
              WebDriverWait(browser, 3).until(EC.alert_is_present(), "not alert 'Congrats'")
              alert = browser.switch_to.alert
              assert "Congrats" in alert.text
              alert.accept()
        except TimeoutException:
              assert False 

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
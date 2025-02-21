from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os
from faker import Faker
from selenium.webdriver.support.ui import Select
from Bibliotiki import *

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_tabs():
    try: 
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(link)

        button_tab = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_tab.click()

        time.sleep(1)
        # alert = browser.switch_to.alert
        # alert.accept()
        old_tab = browser.window_handles[0]
        new_tab = browser.window_handles[1]
        browser.switch_to.window(new_tab)

        input_value = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text

        input_answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
        input_answer.send_keys(calc(input_value))

        # browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
        # browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
        # browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')


        button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_submit.click()
        try:
                  WebDriverWait(browser, 3).until(EC.alert_is_present(), "not alert 'Congrats'")
                  alert = browser.switch_to.alert
                  assert "Congrats" in alert.text
                  alert.accept()
        except TimeoutException:
                  assert False
      

        #можно создать файл в питоне
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
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os
from faker import Faker
from selenium.webdriver.support.ui import Select
from Bibliotiki import *

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_get_1():
    try: 

        browser = webdriver.Chrome()
        # говорим WebDriver ждать все элементы в течение 5 секунд
        browser.implicitly_wait(5)

        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        button = browser.find_element(By.ID, "book")
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        Price = WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"), "$100") )
        button.click()

        # следующий кусок написала нейросеть
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = str(math.log(abs(12*math.sin(int(x)))))

        input_field = browser.find_element(By.ID, "answer")
        input_field.send_keys(y)

        submit_button = browser.find_element(By.ID, "solve")
        submit_button.click()
        try:
                  WebDriverWait(browser, 3).until(EC.alert_is_present(), "not alert 'Congrats'")
                  alert = browser.switch_to.alert
                  assert "Congrats" in alert.text
                  alert.accept()
        except TimeoutException:
                  assert False
                # title_is
                # title_contains
                # presence_of_element_located
                # visibility_of_element_located
                # visibility_of
                # presence_of_all_elements_located
                # text_to_be_present_in_element
                # text_to_be_present_in_element_value
                # frame_to_be_available_and_switch_to_it
                # invisibility_of_element_located
                # element_to_be_clickable
                # staleness_of
                # element_to_be_selected
                # element_located_to_be_selected
                # element_selection_state_to_be
                # element_located_selection_state_to_be
                # alert_is_present
        # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
        # button = WebDriverWait(browser, 5).until_not( EC.element_to_be_clickable((By.ID, "verify"))  )
        
        # message = browser.find_element(By.ID, "verify_message")

        # assert "successful" in message.text

        
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
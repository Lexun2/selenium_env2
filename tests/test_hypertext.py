from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from Bibliotiki import *

def test_hyper():
        link = "http://suninjuly.github.io/find_link_text"

        try:
            browser = webdriver.Chrome()
            browser.get(link)

            link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
            link.click()

            input1 = browser.find_element(By.TAG_NAME, "input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.NAME, "last_name")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CLASS_NAME, "city")
            input3.send_keys("Smolensk")
            input4 = browser.find_element(By.ID, "country")
            input4.send_keys("Russia")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            try:
                  WebDriverWait(browser, 3).until(EC.alert_is_present(), "not alert 'Congrats'")
                  alert = browser.switch_to.alert
                  assert "Congrats" in alert.text
                  alert.accept()
            except TimeoutException:
                  assert False

        finally:
            time.sleep(1)
            browser.quit()

# не забываем оставить пустую строку в конце файла
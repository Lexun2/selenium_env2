from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
from Bibliotiki import *

def test_big_anketa():
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/huge_form.html")
            fake = Faker('ru_RU')
            elements = browser.find_elements(By.TAG_NAME, "input")
            for element in elements:
                element.send_keys(fake.word())

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
            # успеваем скопировать код за 30 секунд
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()

        # не забываем оставить пустую строку в конце файла
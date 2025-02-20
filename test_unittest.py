import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

class TestAbs(unittest.TestCase):

    def fill_form(self, link):
        try: 
            browser = webdriver.Chrome()
            browser.get(link)
            fake=Faker('ru_RU')
            input1 = browser.find_element(By.XPATH,"//label[text()='First name*']/..//input[@class='form-control first' and 'required']")
            input1.send_keys(fake.first_name())
            time.sleep(1)
            input2 = browser.find_element(By.CSS_SELECTOR,".first_block .form-control.second[required]")
            input2.send_keys(fake.last_name())
            time.sleep(1)
            input3 = browser.find_element(By.CSS_SELECTOR,".first_block .form-control.third[required]")
            input3.send_keys(fake.email())
            time.sleep(1)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error registration!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.fill_form(link)        
    
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.fill_form(link)      



if __name__ == "__main__":
    unittest.main()
    # test_abs1()
    # test_abs2()
    # print("All tests passed!")
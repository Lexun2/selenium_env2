from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

try: 
    link = "http://suninjuly.github.io/registration1.html"
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
     
    ...

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполнение поля "Имя"
    nameInput = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
    nameInput.send_keys("Name")

    # Заполнение поля "Фамилия"
    lastnameInput = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
    lastnameInput.send_keys("Surname")

    # Заполнение поля "Email"
    emailInput = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
    emailInput.send_keys("pochta@mail.com")
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
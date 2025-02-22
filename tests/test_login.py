import pytest, json, time
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="session")
def autorization():
    # Открываем файл с конфигом в режиме чтения
    with open('tests\\stepik.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


def test_guest_should_see_login_link(browser, autorization):
    login = autorization['login_stepik']
    password = autorization['password_stepik']
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(20)
    button_vhod = browser.find_element(By.ID,"ember471")
    button_vhod.click()
    input_login = browser.find_element(By.CSS_SELECTOR,"input[name='login']")
    input_login.send_keys(login)
    input_password = browser.find_element(By.CSS_SELECTOR,"input[name='password']")
    input_password.send_keys(password)
    button_submit = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    time.sleep(5)
    button_submit.click()
    time.sleep(100)
import pytest, json, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from Bibliotiki import *


@pytest.fixture(scope="session")
def autorization():
    # Открываем файл с конфигом в режиме чтения
    with open('tests\\stepik.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.mark.parametrize("link", [
# "https://stepik.org/lesson/236895/step/1",
# "https://stepik.org/lesson/236896/step/1",
# "https://stepik.org/lesson/236897/step/1",
# "https://stepik.org/lesson/236898/step/1",
# "https://stepik.org/lesson/236899/step/1",
# "https://stepik.org/lesson/236903/step/1",
# "https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
                                    ])
def test_guest_should_see_login_link(browser, autorization,link):
    login = autorization['login_stepik']
    password = autorization['password_stepik']
    if login=="test@test.ru": pytest.xfail()
    browser.get(link)
      
    try:
                button_vhod = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH,"//nav[@class='navbar']/a[text()='Войти']")), "not visible element 'Enter'")
    except TimeoutException:
                assert False, "Button 'Enter' is not visible!"
    button_vhod.click()    
    try:
                input_login = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='login']")), "not visible element 'Login'")
    except TimeoutException:
                assert False, "Element input 'Login' is not visible!"
    input_login.send_keys(login)
    input_password = browser.find_element(By.CSS_SELECTOR,"input[name='password']")
    input_password.send_keys(password)
    button_submit = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button_submit.click()

    try:
                button_again = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.again-btn")), "not visible element 'Button 'Again'")
                button_again.click() 
    except TimeoutException:
                pass
   
    try:
                input_text = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[placeholder='Напишите ваш ответ здесь...']")), "not visible element 'input answer'")
    except TimeoutException:
                assert False, "Element 'input answer' not visible!"
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_text)
    input_text.clear()
    answer = math.log(int(time.time()))
    input_text.send_keys(float(answer))
  
    try:
                button_submit = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.submit-submission")), "not visible element 'button'")
    except TimeoutException:
                assert False, "Element 'button' not visible!"
   
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
  
    button_submit.click()

    try:
                result_text = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint')), "not visible element 'Correct!'")
    except TimeoutException:
                assert False, "answer do not visible"
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", result_text)
 
    assert "Correct!" ==  result_text.text

    # The owls are not what they seem! OvO

    # pytest -x           # stop after first failure
    # pytest --maxfail=2  # stop after two failures
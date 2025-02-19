from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os
from faker import Faker
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    # browser.get(link)
    input_name = browser.find_element(By.NAME="firstname")
    input_name.send_keys("Aleks")



    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)



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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
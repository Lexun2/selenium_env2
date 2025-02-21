import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
count_test = 0
# Для фикстур можно задавать область покрытия фикстур scope. 
# Допустимые значения: “function”, “class”, “module”, “session”. 
# Соответственно, фикстура будет вызываться 
# один раз для тестового метода, 
# один раз для класса, 
# один раз для модуля,
# один раз для всех тестов, запущенных в данной сессии. 
# Параметр autouse=True, который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова: 

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    global count_test
    count_test+=1
    print(f"\nЗапускаем Тест № {count_test}\n")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
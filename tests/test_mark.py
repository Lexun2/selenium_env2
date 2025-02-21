import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
count_test = 0
 
# pytest -s -v tests\test_mark.py -m smoke                  smoke- название маркировки
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию
# pytest -s -v tests\test_mark.py -m "not all_class"
# Для запуска тестов с разными метками можно использовать логическое ИЛИ
# pytest -s -v tests\test_mark.py -m "smoke or regression"

# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И и наш маркер win10 из pytest.ini
# pytest -s -v -m "smoke and win10" test_fixture81.py
# Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip

@pytest.fixture(scope="class")
def browser():
    # print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    # print("\nquit browser")
    driver.quit()

# @pytest.fixture(autouse=True)
# def prepare_data():
#     global count_test
#     count_test+=1
#     # print(f"\nЗапускаем Тест № {count_test}\n")

@pytest.mark.all_class
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.win10
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.skip
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
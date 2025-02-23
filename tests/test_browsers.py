from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="session", autouse = True)
def final():
    print("Начали тесты!!!")
    yield
    print("Закончили тесты!!!")

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

# pytest tests\test_firefox.py -s -v --browser_name firefox

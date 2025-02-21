from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        print("test 1 in class")
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        print("test 2 in class")
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        print("test 1 not in class")
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        print("test 2 not in class")
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

#         префиксы setup_*, teardown_* отвечают за порядок исполнения фикстур: до чего-то, после чего-то.
# постфиксы *_class, *_method и другие отвечают за уровень применения фикстур: ко всему классу, к каждому методу в классе и тд.
# Исходя их логики выше:

# setup_class выполняется один раз перед запуском всех тестовых методов в классе
# teardown_class выполянется один раз после
# setup_method выполняется перед запуском каждого тестового метода в классе
# teardown_method выполняется каждый раз после
# Про декоратор:

# @classmethod декоратор, использованный для удобства чтения кода. Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.
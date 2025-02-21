from Bibliotiki import *


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

# py.test test_sample.py --collect-only # собирает информацию тестового набора

# py.test test_sample.py -v # выводит вербозные сообщения

# py.test -q test_sample.py # опустить вывод имени файла

# python -m pytest -q test_sample.py # вызов pytest через python

# py.test --markers # показать доступные маркеры

# # Для того чтобы создать маркер многократного использования.
# /*
# # содержимое pytest.ini
# [pytest].
# маркеры =
#     webtest: пометить тест как webtest.
# */

# py.test -k "TestClass, а не test_one" # запускать только тесты с именами, которые соответствуют "строковому выражению"

# py.test test_server.py::TestClass::test_method # cnly run tests that match the node ID

# py.test -x # останавливаться после первой неудачи

# py.test --maxfail=2 # останавливаться после двух неудач

# py.test --showlocals # показывать локальные переменные в трассировках
# py.test -l # (сокращение)

# py.test --tb=long # информативное форматирование трассировки по умолчанию
# py.test --tb=native # форматирование стандартной библиотеки Python
# py.test --tb=short # более короткий формат возвратов к трассировке
# py.test --tb=line # только одна строка для каждого сбоя
# py.test --tb=no # отсутствие вывода трассировки

# py.test -x --pdb # при первом сбое сброс в PDB, затем завершение сеанса тестирования

# py.test --durations=10 # список 10 самых медленных длительностей теста.

# py.test --maxfail=2 -rf # выход после двух сбоев, сообщение о сбое.

# py.test -n 4 # посылать тесты на несколько процессоров

# py.test -m slowest # запускать тесты с декоратором @pytest.mark.slowest или slowest = pytest.mark.slowest; @slowest

# py.test --traceconfig # выяснить, какие плагины py.test активны в вашем окружении.

# py.test --instafail # если установлен pytest-instafail, показывать ошибки и сбои мгновенно, а не ждать окончания набора тестов.


# if __name__ == "__main__":
#     unittest.main()
    # test_abs1()
    # test_abs2()
    # print("All tests passed!")
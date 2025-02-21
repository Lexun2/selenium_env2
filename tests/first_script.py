from Bibliotiki import *

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

def test_script():
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        browser = webdriver.Chrome()

        # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
        time.sleep(1)

        # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        browser.get("https://stepik.org/lesson/25969/step/12")
        time.sleep(1)

        # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
        # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
        # Ищем поле для ввода текста
        textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")

        # Напишем текст ответа в найденное поле
        textarea.send_keys("get()")
        time.sleep(1)

        # Найдем кнопку, которая отправляет введенное решение
        submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")

        # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
        submit_button.click()
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(), "not alert 'Congrats'")
            alert = browser.switch_to.alert
            assert "Congrats" in alert.text
            alert.accept()
        except TimeoutException:
            assert False

        # После выполнения всех действий мы должны не забыть закрыть окно браузера
        browser.quit()

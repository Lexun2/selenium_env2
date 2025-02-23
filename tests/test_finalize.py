import pytest

#смотри логи выполнения принтов


# Первый вариант через yield
@pytest.fixture
def my_fixture():
    print("\n-------------------------------\nСпособ через yield:\nОткрыл соединение с БД")
    print("Тут много работы")
    prin    #ошибка в коде
    yield                                           #через yield Соединение с БД не закроется при ошибке другого разраба в коде
    print("\nЗакрыл соединение с БД")


def test_1(my_fixture):
    print("\nРаботаю с бд................")
    1/0



# Второй вариант через try
@pytest.fixture
def my_fixture3(request):
    try:
        print("\n-------------------------------\nСпособ через yield в try:\nОткрыл соединение с БД")
        print("Тут много работы")
        prin     #ошибка в коде
        2/0
        yield                                           #через yield в try Соединение с БД закроется даже при ошибке другого разраба в коде
    finally:
        print("\nЗакрыл соединение с БД")


def test_3(my_fixture3):
    print("\nРаботаю с бд................")
    1/0


# Третий вариант через addFinalizer
@pytest.fixture
def my_fixture2(request):
    print("\n-------------------------------\nСпособ через addfinalizer:\nОткрыл соединение с БД")
    def final():
        print("\nЗакрыл соединение с БД")           #через addFinalizer Соединение с БД закроется даже при ошибке другого разраба в коде
    request.addfinalizer(final)
    print("Тут много работы")
    2/0
    prin     #ошибка в коде
    


def test_2(my_fixture2):
    print("\nРаботаю с бд................")
    1/0



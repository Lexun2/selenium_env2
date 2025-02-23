import pytest
# Первый вариант через yield
@pytest.fixture
def my_fixture():
    print("\nОткрыл соединение с БД")
    yield                                           #через yield Соединение с БД не закроется при ошибке другого разраба в коде
    print("\nЗакрыл соединение с БД")


def test_1(my_fixture):
    print("\nРаботаю с бд................")




# Второй вариант через addFinalizer
@pytest.fixture
def my_fixture2(request):
    print("\nОткрыл соединение с БД")
    def final():
        print("\nЗакрыл соединение с БД")           #через addFinalizer Соединение с БД закроется даже при ошибке другого разраба в коде
    request.addfinalizer(final)
    


def test_2(my_fixture2):
    print("\nРаботаю с бд................")
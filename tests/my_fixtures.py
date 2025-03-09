import pytest

c = 0

@pytest.fixture(autouse=True)
def print_info_about_testing(request):
    global c
    c=c+1
    # request.fspath  - полный путь исполняемого теста
    # request.node.module.__name__ - название файла теста
    # request.node.name - название функции теста
    print(f"\nНачали выполнять тест #{c}, файл {request.node.module.__name__}, тест {request.node.name}")
    yield
    print(f"\nЗакончили выполнять тест #{c}")
    print("\n--------------------------------------------------------------------\n")
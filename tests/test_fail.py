import pytest, random


@pytest.mark.parametrize("number", [1,2,3,3,-3,0])
def test_failure(number):
    print(number)
    try:
        1/number
    except ZeroDivisionError:
        pass

# pytest -s --maxfail=2  tests\test_fail.py
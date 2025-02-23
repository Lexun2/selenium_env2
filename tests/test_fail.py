import pytest, random

@pytest.mark.parametrize("hell", [random.randint(-3,7) for i in range(5)])
def test_failure(hell):
    1/hell

# pytest -s --maxfail=2  tests\test_fail.py
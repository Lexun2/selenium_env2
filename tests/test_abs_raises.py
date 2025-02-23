
import pytest, math

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a Number"

def test_abs2():
    assert abs(-42) != -42, "Should be absolute value of a Number"




def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0




def test_division_by_char():
    with pytest.raises(TypeError):
        1 / "a"
        


def test_index_raise():
    a=["1","2","3"]
    with pytest.raises(IndexError):
        a[3]




def test_foo():
    slov = {
        'a': '1',
        'b': '2'
         }
    with pytest.raises(KeyError) as exc:
        value = slov['cobol']
    assert exc.type == KeyError
    assert exc.match('obo')
    if exc is not None :
        print(f"\ntest foo:\n{exc}")




def test_value_error():
    with pytest.raises(ValueError) as exc:
        math.sqrt(-16)
    assert exc.type == ValueError




def test_get_assert_error():
    with pytest.raises(AssertionError) as exc:
        assert 1==2
    print(exc.value)
    print(exc.match)




def test_exceptions():
    slov = {
        'a': '1',
        'b': '2'
         }
    try:
        a=slov['c']
    except KeyError:
        print('missing foo or bar')
    except ValueError:
        print('missing value')
    except IndexError:
        print('missing index')
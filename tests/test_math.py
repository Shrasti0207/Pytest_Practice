import pytest

def test_one_plus_one(): 
    assert 1+1 == 2

def test_one_plus_two(): 
    a = 1
    b = 2
    assert a + b == 3

def  test_divide_by_zer0():             #handle the exception using pytest.raises
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

numbers = {
    (2,3,6),
    (3,0,0),
    (1,1,1)
}

@pytest.mark.parametrize('a, b, product', numbers)
def test_multiplication(a, b, product):
    assert a * b == product
import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

#failing test
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

@pytest.mark.math
def test_divide_by_zero():
    #with block stores exception as e
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)

 
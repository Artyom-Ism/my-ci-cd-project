from calculator import add, subtract, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(-5, 10) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
    assert subtract(10, 10) == 0
    assert subtract(-2, -3) == 1


def test_mul():
    assert mul(7, 3) == 21
    assert mul(5, 2) == 10
    assert mul(9, 9) == 81
    assert mul(8, 2) == 16
    
def test_div():
    assert div(9, 3) == 3
    assert div(21, 3) == 7
    assert div(6, 2) == 3
    assert div(8, 2) == 4

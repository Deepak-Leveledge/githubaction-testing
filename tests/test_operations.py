from src.math_operation import Add, Subtract, Multiply



def test_add():
    assert Add(2, 3) == 5
    assert Add(-1, 1) == 0
    assert Add(0, 0) == 0

def test_subtract():
    assert Subtract(5, 2) == 3
    assert Subtract(2, 5) == -3
    assert Subtract(0, 0) == 0

def test_multiply():
    assert Multiply(2, 3) == 6
    assert Multiply(-1, 1) == -1
    assert Multiply(0, 5) == 0
    assert Multiply(3, 0) == 0
    assert Multiply(1, 1) == 1
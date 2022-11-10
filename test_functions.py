import math

from functions import add, product, is_palindrom


# test jednostkowy
def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.3) == 9.6
    assert math.fabs(add(0.1, 0.2) - 0.3) < 0.0000001  # uwaga na float!


def test_product():
    assert product(5, 5) == 25
    assert product(5, 2.5) == 12.5
    assert product(0, 0) == 0


def test_is_palindrom():
    assert is_palindrom("Ala")
    assert is_palindrom('Kobyła ma mały bok')
    assert not is_palindrom("rak")

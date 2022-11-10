from calc import add


def test_add():
    assert add(4, 7) == 11
    assert add(0, 0) == 0

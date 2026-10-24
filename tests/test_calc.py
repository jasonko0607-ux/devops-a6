from calc import add, subtract, greeting


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_greeting():
    assert greeting("DevOps") == "Hello, DevOps!"

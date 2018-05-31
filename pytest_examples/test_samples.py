

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (2, 1, 3) == (1, 2, 3)

"""
Assert statements to test a function
"""


def square(x):
    return x**2


def test_square():
    assert square(-1) == 1
    assert square(2) == 4
    assert square(5) == 24      # this will cause an AssertionError
    print("Alle Tests bestanden!")


test_square()

# Tests a function with multiple functions via pytest


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


def test_positive():
    assert square(3) == 9
    assert square(2) == 4
    assert square(1) == 1


def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


if __name__ == "__main__":
    main()

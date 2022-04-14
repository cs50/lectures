# Tests a function with one function


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


def test_square():
    assert square(3) == 9
    assert square(2) == 4
    assert square(1) == 1
    assert square(0) == 0
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


if __name__ == "__main__":
    main()

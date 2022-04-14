# Tests a function using assert


def main():
    assert square(2) == 4
    assert square(3) == 9


def square(n):
    return n * n



if __name__ == "__main__":
    main()

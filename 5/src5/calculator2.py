# Catches exceptions


def main():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


def square(n):
    return n * n



if __name__ == "__main__":
    main()

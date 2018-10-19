# Fails to swap two integers


def main():
    x = 1
    y = 2

    print(f"x is {x}, y is {y}")
    swap(x, y)
    print(f"x is {x}, y is {y}")


def swap(a, b):
    tmp = a
    a = b
    b = tmp


if __name__ == "__main__":
    main()

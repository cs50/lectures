# Demonstrates conditional expressions (ternary operators)


def main():
    x = int(input("What's x? "))
    print("Even" if is_even(x) else "Odd")


def is_even(n):
    return True if n % 2 == 0 else False


if __name__ == "__main__":
    main()

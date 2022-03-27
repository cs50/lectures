# Demonstrates returning the value of a Boolean expression


def main():
    x = int(input("What's x? "))
    print("Even" if is_even(x) else "Odd")


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()

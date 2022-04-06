def main():
    x = get_integer()
    if x < 0:
        print("x is negative")
    elif x > 0:
        print("x is positive")
    else:
        print("x is zero")


def get_integer():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("Not an integer")


main()

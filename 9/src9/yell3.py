# Uses map with named function


def main():
    yell("This", "is", "CS50")


def uppercase(s):
    return s.upper()


def yell(*words):
    uppercased = map(uppercase, words)
    print(*uppercased)


if __name__ == "__main__":
    main()

# Uses map with lambda function


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(lambda arg: arg.upper(), words)
    print(*uppercased)


if __name__ == "__main__":
    main()

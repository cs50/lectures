# Uses list comprehension


def main():
    yell("hello", "world", sep=" @#$% ")


def yell(*args, **kwargs):
    caps = [arg.upper() for arg in args]
    print(*caps, **kwargs)


if __name__ == "__main__":
    main()

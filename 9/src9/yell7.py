# Uses map with named function


def main():
    yell("hello", "world", sep=" @#$% ")


def uppercase(s):
    return s.upper()


def yell(*args, **kwargs):
    caps = map(uppercase, args)
    print(*caps, **kwargs)


if __name__ == "__main__":
    main()

# Uses map with lambda function


def main():
    yell("hello", "world", sep=" @#$% ")


def yell(*args, **kwargs):
    caps = map(lambda arg: arg.upper(), args)
    print(*caps, **kwargs)


if __name__ == "__main__":
    main()

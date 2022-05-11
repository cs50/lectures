# Uses print's args, kwargs


def main():
    yell("hello", "world", sep=" @#$% ")


def yell(*args, **kwargs):
    caps = []
    for arg in args:
        caps.append(arg.upper())
    print(*caps, **kwargs)


if __name__ == "__main__":
    main()

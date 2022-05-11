# Also accepts named parameter


def main():
    yell("hello", "world")


def yell(*words, sep=" "):
    caps = []
    for word in words:
        caps.append(word.upper())
    print(sep.join(caps))


if __name__ == "__main__":
    main()

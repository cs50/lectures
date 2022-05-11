# Prints a list of arbitrarily many args in all caps


def main():
    yell("hello", "world")


def yell(*words):
    caps = []
    for word in words:
        caps.append(word.upper())
    print(" ".join(caps))


if __name__ == "__main__":
    main()

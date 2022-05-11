# Adds **kwargs


def main():
    yell("hello", "world", sep=" @#$% ")


def yell(*words, **kwargs):
    caps = []
    for word in words:
        caps.append(word.upper())
    print(kwargs["sep"].join(caps))


if __name__ == "__main__":
    main()

# Sums a range of numbers recursively


from cs50 import get_int


def main():
    while True:
        n = get_int("Positive integer: ")
        if n > 0:
            break
    answer = sigma(n)
    print(answer)


def sigma(m):
    """Return sum of 1 through m"""
    if m <= 0:
        return 0
    else:
        return m + sigma(m - 1)


if __name__ == "__main__":
    main()

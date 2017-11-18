# Sums a range of numbers iteratively


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
    sum = 0
    for i in range(m + 1):
        sum += i
    return sum


if __name__ == "__main__":
    main()

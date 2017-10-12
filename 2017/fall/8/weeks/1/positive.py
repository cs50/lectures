# Abstraction and scope

from cs50 import get_int


def main():
    i = get_positive_int("positive integer, please: ")
    print(f"{i} is a positive integer")


def get_positive_int(prompt):
    """Prompt user for positive integer"""
    while True:
        n = get_int(prompt)
        if n > 0:
            break
    return n


if __name__ == "__main__":
    main()

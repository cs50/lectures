# Iterative binary search

import sys
from cs50 import get_string

# Names in a phone book
book = [
    "Chen",
    "Kernighan",
    "Leitner",
    "Lewis",
    "Malan",
    "Muller",
    "Seltzer",
    "Shieber",
    "Smith"]


def main():

    # Prompt user for name
    name = get_string("Name: ")

    # Search for name
    left, right = 0, len(book) - 1
    while left <= right:
        middle = (left + right) // 2
        if name == book[middle]:
            print(f"Calling {name}")
            sys.exit(0)
        elif name < book[middle]:
            right = middle - 1
        elif name > book[middle]:
            left = middle + 1
    print("Quitting")
    sys.exit(1)


if __name__ == "__main__":
    main()

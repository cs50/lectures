# Recursive binary search

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
    if search(name, book):
        print(f"Calling {name}")
    else:
        print("Quitting")


def search(name, names):
    """Search names for name"""

    # No more names to search
    if not names:
        return False

    # Look at middle
    middle = len(names) // 2
    if name == names[middle]:
        return True

    # Search left half
    elif name < names[middle]:
        return search(name, names[:middle])

    # Search right half
    elif name > names[middle]:
        return search(name, names[middle + 1:])


if __name__ == "__main__":
    main()

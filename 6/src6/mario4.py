# Prints a square of bricks, sized as specified by user

from cs50 import get_int

# Prompt user for a positive number
while True:
    n = get_int("Positive number: ")
    if n > 0:
        break

# Print out this many rows
for i in range(n):

    # Print out this many columns
    for j in range(n):
        print("#", end="")
    print()

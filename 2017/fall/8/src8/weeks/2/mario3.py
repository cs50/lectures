# Prints a positive number of question marks, as specified by user

from cs50 import get_int

# Prompt user for a positive number
while True:
    n = get_int("Positive number: ")
    if n > 0:
        break

# Print out that many bricks
for i in range(n):
    print("#")

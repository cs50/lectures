# Prints any number of question marks, as specified by user

from cs50 import get_int

n = get_int("Number: ")
for i in range(n):
    print("?", end="")
print()

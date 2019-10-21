# Prints string character by character

from cs50 import get_string

s = get_string("Input:  ")
print("Output: ", end="")
for c in s:
    print(c, end="")
print()

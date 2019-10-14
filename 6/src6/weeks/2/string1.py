# Prints string char by char, one per line

from cs50 import get_string

s = get_string("Input: ")
print("Output:");
for c in s:
    print(c)

# Explicitly casts chars to ints

from cs50 import get_string

s = get_string("Name: ")
for c in s:
    print(f"{c} {ord(c)}")

# Explicitly casts chars to ints

from cs50 import get_string

s = get_string("String: ")
for c in s:
    print(f"{c} {ord(c)}")

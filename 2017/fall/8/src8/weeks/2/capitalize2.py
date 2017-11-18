# Capitalizes string using str method

from cs50 import get_string

s = get_string()
for c in s:
    print(c.upper(), end="")
print()

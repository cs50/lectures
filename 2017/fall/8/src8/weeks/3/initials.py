# Extracts a user's initials

from cs50 import get_string

s = get_string("Name: ")
initials = ""
for c in s:
    if c.isupper():
        initials += c
print(initials)

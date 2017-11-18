# Compares two strings for equality

from cs50 import get_string

# Get two strings
s = get_string("s: ")
t = get_string("t: ")

# Compare strings for equality
if s == t:
    print("same")
else:
    print("different")

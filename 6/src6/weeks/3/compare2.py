# Compares two strings for equality while checking for errors

import sys
from cs50 import get_string

# Get a string
s = get_string("s: ")
if s is None:
    sys.exit(1)

# Get another string
t = get_string("t: ")
if t is None:
    sys.exit(1)

# Compare strings for equality
if s == t:
    print("same")
else:
    print("different")

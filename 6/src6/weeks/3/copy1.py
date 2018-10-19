# Capitalizes a copy of a string while checking for errors

import sys
from cs50 import get_string

# Get a string
s = get_string("s: ")
if not s:
    sys.exit(1)

# Capitalize first letter in copy
t = s.capitalize()

# Print strings
print(f"s: {s}")
print(f"t: {t}")

sys.exit(0)

# Implements linear search for numbers

import sys

# A list of numbers
numbers = [4, 8, 15, 16, 23, 42]

# Search for 50
if 50 in numbers:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1)

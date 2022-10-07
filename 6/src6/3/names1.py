# Implements linear search for names using `in`

import sys

# A list of names
names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

# Ask for name
name = input("Name: ")

# Search for name
if name in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)

# Implements linear search for names

import sys

# A list of names
names = ["EMMA", "RODRIGO", "BRIAN", "DAVID"]

# Search for EMMA
if "EMMA" in names:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1)

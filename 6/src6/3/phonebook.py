# Implements a phone book

import sys

people = {
    "EMMA": "617-555-0100",
    "RODRIGO": "617-555-0101",
    "BRIAN": "617-555-0102",
    "DAVID": "617-555-0103"
}

# Search for EMMA
if "EMMA" in people:
    print(f"Found {people['EMMA']}")
    sys.exit(0)
print("Not found")
sys.exit(1)

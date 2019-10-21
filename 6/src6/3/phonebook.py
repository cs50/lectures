# Implements a phone book

import sys

people = []
people.append({"name": "EMMA", "number": "617-555-0100"})
people.append({"name": "RODRIGO", "number": "617-555-0101"})
people.append({"name": "BRIAN", "number": "617-555-0102"})
people.append({"name": "DAVID", "number": "617-555-0103"})

# Search for EMMA
for person in people:
    if person["name"] == "EMMA":
        print(f"Found {person['number']}")
        sys.exit(0)
print("Not found")
sys.exit(1)

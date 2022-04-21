# Uses re.search

import re

before = input("Before: ").strip()

matches = re.search("^(\d{3})-(\d{3})-(\d{4})$", before)
if matches:
    print(f"After: ", matches.group(1), matches.group(2), matches.group(3), sep="")

matches = re.search("^\((\d{3})\) (\d{3})-(\d{4})$", before)
if matches:
    print(f"After: ", matches.group(1), matches.group(2), matches.group(3), sep="")

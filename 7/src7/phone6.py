# Uses walrus operator

import re

before = input("Before: ").strip()

if matches := re.search("^(\d{3})-(\d{3})-(\d{4})$", before):
    print(f"After: ", matches.group(1), matches.group(2), matches.group(3), sep="")

elif matches := re.search("^\((\d{3})\) (\d{3})-(\d{4})$", before):
    print(f"After: ", matches.group(1), matches.group(2), matches.group(3), sep="")

# Uses re.search

import re

name = input("Name: ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    first, last = matches.groups()
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

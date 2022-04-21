# Uses walrus operator

import re

name = input("Name: ").strip()
if matches := re.search("^(.+), (.+)$", name):
    first, last = matches.groups()
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

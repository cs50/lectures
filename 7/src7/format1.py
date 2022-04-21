# Uses re.search

import re

name = input("What's your name? ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")

# Uses re.sub

import re

before = input("Before: ").strip()

after = re.sub("[() -]", "", before)

print(f"After: {after}")

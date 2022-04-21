# Uses re.sub with \d

import re

before = input("Before: ").strip()

after = re.sub("[^\d]", "", before)

print(f"After: {after}")

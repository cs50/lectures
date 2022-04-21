# Adds .*

import re

email = input("What's your email? ").strip().lower()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")

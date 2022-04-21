# Adds ^ and $ to regex

import re

email = input("What's your email? ").strip().lower()

if re.search("^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

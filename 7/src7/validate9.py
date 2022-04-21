# Adds character class

import re

email = input("What's your email? ").strip()

if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

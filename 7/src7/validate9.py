# Adds character class, removes lower()

import re

email = input("What's your email? ").strip()

if re.search("^[a-zA-z0-9_]+@[a-zA-z0-9_]+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

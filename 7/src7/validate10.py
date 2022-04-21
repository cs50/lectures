# Replaces character class with \w

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

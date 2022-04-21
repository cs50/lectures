# Validates email address by checking for @ with regex

import re

email = input("What's your email? ").strip().lower()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

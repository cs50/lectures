# Ignores query and fragment

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))

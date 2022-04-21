# Allows for http and www.

import re

url = input("URL: ").strip()

username = re.sub("^https?://(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

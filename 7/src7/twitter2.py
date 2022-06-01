# Uses re.sub

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")

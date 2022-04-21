# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

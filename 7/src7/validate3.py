# Validates email address by checking whether domain ends with .edu

email = input("What's your email? ").strip().lower()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

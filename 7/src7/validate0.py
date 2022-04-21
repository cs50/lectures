# Validates email address by checking for @

email = input("What's your email? ").strip().lower()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

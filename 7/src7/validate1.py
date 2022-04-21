# Validates email address by checking for . too

email = input("What's your email? ").strip().lower()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

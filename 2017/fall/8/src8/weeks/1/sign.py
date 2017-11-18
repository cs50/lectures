# Conditions and relational operators

from cs50 import get_int

# Prompt user for number
i = get_int("number: ")

# Check sign of number
if i < 0:
    print("negative")
elif i > 0:
    print("positive")
else:
    print("zero")

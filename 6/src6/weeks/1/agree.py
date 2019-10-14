# Logical operators

from cs50 import get_char

# Prompt user to agree
c = get_char("Do you agree?\n")

# Check whether agreed
if c == "Y" or c == "y":
    print("Agreed.")
elif c == "N" or c == "n":
    print("Not agreed.")

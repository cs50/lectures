# Logical operators, using lists

# Prompt user to agree
s = input("Do you agree? ").lower()

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")

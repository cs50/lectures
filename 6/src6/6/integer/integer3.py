# Handles exception

# Prompt user for an integer
try:
    n = int(input("Input: "))
except ValueError:
    print("Not integer.")
else:
    print("Integer.")

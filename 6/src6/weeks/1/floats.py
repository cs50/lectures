# Floating-point arithmetic

from cs50 import get_float

# Prompt user for x
x = get_float("x: ")

# Prompt user for y
y = get_float("y: ")

# Perform division
print(f"x / y = {(x / y):.50f}")

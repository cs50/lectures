# Integer arithmetic

from cs50 import get_int

# Prompt user for x
x = get_int("x: ")

# Prompt user for y
y = get_int("y: ")

# Perform arithmetic
print(f"{x} plus {x} is {x + y}")
print(f"{x} minus {y} is {x - y}")
print(f"{x} times {y} is {x * y}")
print(f"{x} truly divided by {y} is {x / y}")
print(f"{x} floor-divided by {y} is {x // y}")
print(f"remainder of {x} divided by {y} is {x % y}")

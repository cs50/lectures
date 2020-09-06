import cs50

# prompt user for x
print("x is ", end="")
x = cs50.get_float()

# prompt user for y
print("y is ", end="")
y = cs50.get_float()

# perform division for user
print("{} divided by {} is {}".format(x, y, x / y))

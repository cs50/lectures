import cs50

# prompt user for x
print("x is ", end="")
x = cs50.get_int()

# prompt user for y
print("y is ", end="")
y = cs50.get_int()

# perform calculations for user
print("{} plus {} is {}".format(x, y, x + y))
print("{} minus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided by {} is {}".format(x, y, x / y))
print("{} divided by {} (and floored) is {}".format(x, y, x // y))
print("remainder of {} divided by {} is {}".format(x, y, x % y))

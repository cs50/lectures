import cs50

# prompt user for x
print("x is ", end="")
x = cs50.get_int()

# prompt user for y
print("y is ", end="")
y = cs50.get_int()

# calculate sum for user
print("sum is {}".format(x + y))

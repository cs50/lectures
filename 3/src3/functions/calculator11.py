# Demonstrates floating-point imprecision

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.50f}")

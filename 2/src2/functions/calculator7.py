# Demonstrates floating-point imprecision (e.g., 1 / 3)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.50f}")

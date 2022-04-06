try:
    x = int(input("What's x? "))
except ValueError:
    print("Not an integer")
else:
    if x < 0:
        print("x is negative")
    elif x > 0:
        print("x is positive")
    else:
        print("x is zero")

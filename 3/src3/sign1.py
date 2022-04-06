try:
    x = int(input("What's x? "))
    if x < 0:
        print("x is negative")
    elif x > 0:
        print("x is positive")
    else:
        print("x is zero")
except ValueError:
    print("Not an integer")

# Demonstrates defining a function with a parameter with a default value


def greet(who="world"):
    print("hello,", who)


name = input("What's your name? ")
greet(name)

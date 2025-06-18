# Demonstrates defining a function with a parameter with a default value


def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)

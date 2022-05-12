# Demonstrates TypeError


def meow(n):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)

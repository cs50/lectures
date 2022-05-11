# Argument ... has incompatible type


def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)

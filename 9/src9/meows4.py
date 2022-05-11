# ... does not return a value


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")

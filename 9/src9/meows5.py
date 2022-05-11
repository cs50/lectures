# Incompatible types in assignment


def meow(n: int) -> str:
    return "meow\n" * 3


number: int = int(input("Number: "))
meows: int = meow(number)
print(meows, end="")

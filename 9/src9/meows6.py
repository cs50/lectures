# Success


def meow(n: int) -> str:
    return "meow\n" * 3


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

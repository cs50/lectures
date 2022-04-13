# Stores names in a list

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")

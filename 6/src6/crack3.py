with open("dictionary.txt") as file:
    words = file.read().splitlines()
for word in words:
    print(word)

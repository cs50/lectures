# Demonstrates validation of user's input

while True:
    n = int(input("What's n? "))
    if n > 1:
        break

for _ in range(n):
    print("meow")

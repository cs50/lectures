from time import sleep

with open("large", "r") as file:
    for word in file.readlines():
        print(f"Checking {word.rstrip()}...")
        sleep(.1)

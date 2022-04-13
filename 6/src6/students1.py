# Unpacks a list

with open("students0.csv") as file:
    next(file)
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

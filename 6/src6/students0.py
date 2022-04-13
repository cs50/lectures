# Reads a CSV file

with open("students0.csv") as file:
    next(file)
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

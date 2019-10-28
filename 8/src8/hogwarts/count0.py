# Counts number of students in houses

import csv

# Numbers of students in houses
houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

# Count votes
with open("Sorting Hat - Form Responses 1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        houses[row[3]] += 1

# Print counts
for house in houses:
    print(f"{house}: {houses[house]}")

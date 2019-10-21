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
with open("https://docs.google.com/spreadsheets/d/e/2PACX-1vR_wNCw2MHnIbosYHjts0g475X0xcshE3BcmldPCUnyB4isvuDiHUUk0NZdm6-KnVB3Mg7MVBsNlUej/pub?output=csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        houses[row[3]] += 1

# Print counts
for house in houses:
    print(f"{house}: {houses[house]}")

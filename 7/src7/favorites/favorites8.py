# Sorts favorites by value using lambda function

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row["Favorite Language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 0

for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")

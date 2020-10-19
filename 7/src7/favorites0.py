# Prints all titles in CSV using csv.reader

import csv

# Open CSV file
with open("Favorite TV Shows - Form Responses 1.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each title
    for row in reader:
        print(row[1])

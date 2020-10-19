# Prints all titles in CSV using csv.DictReader

import csv

# Open CSV file
with open("Favorite TV Shows - Form Responses 1.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each title
    for row in reader:
        print(row["title"])

import csv

# Prompt user for title
title = input("Title: ")

# Open CSV file
with open("shows2.csv", "r") as input:

    # Create DictReader
    reader = csv.DictReader(input)

    # Iterate over CSV file
    for row in reader:

        # Search for title
        if title.lower() == row["primaryTitle"].lower():
            print(row["primaryTitle"], row["startYear"], row["genres"], sep=" | ")

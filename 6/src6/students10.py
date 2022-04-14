# Writes a CSV file using csv.writer

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

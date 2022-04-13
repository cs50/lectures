# Writes a CSV file using csv.writer

import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("houses.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])

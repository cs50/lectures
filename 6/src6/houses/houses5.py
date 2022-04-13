# Writes a CSV file using csv.DictWriter

import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("houses.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})

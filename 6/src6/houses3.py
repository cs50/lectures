# Reads a CSV file using csv.DictReader

import csv

students = []

with open("houses.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "name": row["name"],
            "house": row["house"]
        })

for student in students:
    print(f"{student['name']} is in {student['house']}")

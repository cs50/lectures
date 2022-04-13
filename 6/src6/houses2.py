# Reads a CSV file using csv.reader

import csv

students = []

with open("houses.csv") as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        students.append({
            "name": row[0],
            "house": row[1]
        })

for student in students:
    print(f"{student['name']} is in {student['house']}")

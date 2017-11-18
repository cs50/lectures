# Demonstrates file I/O

import csv
from cs50 import get_string
from student import Student

# Space for students
students = []

# Prompt for students' names and dorms
for i in range(3):
    name = get_string("name: ")
    dorm = get_string("dorm: ")
    students.append(Student(name, dorm))

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    for student in students:
        writer.writerow((student.name, student.dorm))

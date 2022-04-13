# Sorts a list of dictionaries


students = []

with open("houses.csv") as file:
    next(file)
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def key(s):
    return s["name"]


for student in sorted(students, key=key):
    print(f"{student['name']} is in {student['house']}")

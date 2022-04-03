# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Rob": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

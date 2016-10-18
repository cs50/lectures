import cs50
from student import Student

students = []
for i in range(3):

    print("name: ", end="")
    name = cs50.get_string()

    print("dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

for student in students:
    print("{} is in {}.".format(student.name, student.dorm))

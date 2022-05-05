#


class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def get(cls, name, house):
        name = input("Name: ")
        return cls(name)


def main():
    student = Student.get_student()
    print(student)


if __name__ == "__main__":
    main()

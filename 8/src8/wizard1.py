#


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        return cls(name)


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        if not house:
            raise ValueError("Missing house")
        self.house = house

    @classmethod
    def get(cls):
        student = super().get()
        student.house = input("House: ")
        return student

    ...


class Professor(Wizard):
    ...

    @classmethod
    def get(cls):
        professor = super().get()
        professor.subject = input("Subject: ")
        return professor

    ...


wizard = Wizard.get()
print(wizard)
student = Student.get()
print(student)

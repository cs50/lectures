# Demonstrates inheritance [maybe don't add `if` error-checking]


class Wizard:
    def __init__(self, name, patronus):
        if not name:
            raise ValueError("Missing name")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.patronus = patronus

    def charm(self):
        ...


class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name, patronus)
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject, patronus):
        super().__init__(name, patronus)
        self.subject = subject

    ...

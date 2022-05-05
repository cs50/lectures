# Demonstrates inheritance [add error checking last]


class Wizard:
    def __init__(self, name, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.patronus = patronus


class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name, patronus)
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, department, patronus):
        super().__init__(name, patronus)
        self.department = department

    ...

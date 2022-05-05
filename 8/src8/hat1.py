# Implements sort() with a static method

import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @staticmethod
    def sort(name):
        print(name, "is in", random.choice(Hat.houses))


Hat.sort("Harry")

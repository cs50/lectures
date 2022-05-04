# Returns student as tuple, without unpacking it
# https://scifi.stackexchange.com/q/105992


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()

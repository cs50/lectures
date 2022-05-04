#


def main():
    name = get_name()
    house = get_house()
    print(f"{name} of {house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main()

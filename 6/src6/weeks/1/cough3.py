# Abstraction with parameterization


def main():
    cough(3)


def cough(n):
    """Cough some number of times"""
    for i in range(n):
        print("cough")


if __name__ == "__main__":
    main()

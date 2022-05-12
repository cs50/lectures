# Returns list comprehension

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    return ["🐑" * i for i in range(n)]


if __name__ == "__main__":
    main()

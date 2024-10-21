# Demonstrates __name__

def main():
    meow(3)


# Meow some number of times
def meow(n):
    for i in range(n):
        print("meow")


if __name__ == "__main__":
    main()

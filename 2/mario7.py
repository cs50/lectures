# Prints square of bricks using a function with a loop and str multiplication


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


if __name__ == "__main__":
    main()

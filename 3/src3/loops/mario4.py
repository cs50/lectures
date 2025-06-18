# Prints grid of bricks using a function with a loop and str multiplication


def main():
    for _ in range(3):
        print_row(3)


def print_row(width):
    print("#" * width)


main()

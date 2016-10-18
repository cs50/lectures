def main():
    x = 1
    y = 2

    print("x is {}".format(x))
    print("y is {}".format(y))
    print("Swapping...")
    swap(x, y)
    print("Swapped.")
    print("x is {}".format(x))
    print("y is {}".format(y))

def swap(a, b):
    tmp = a
    a = b
    b = tmp

if __name__ == "__main__":
    main()

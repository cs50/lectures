import cs50

def main():
    i = get_positive_int()
    print("{} is a positive integer".format(i))

def get_positive_int():
    while True:
        print("n is ", end="")
        n = cs50.get_int()
        if n > 0:
            break
    return n

if __name__ == "__main__":
    main()

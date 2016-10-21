import cs50

def main():
    print("x is ", end="")
    x = cs50.get_int()
    print("x^2 is {}".format(square(x)))

def square(n):
    return n**2

if __name__ == "__main__":
    main()

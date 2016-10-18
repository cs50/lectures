import cs50

def main():
    print("x is ", end="")
    x = cs50.get_int()
    print("x^2 is {}".format(x**2))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

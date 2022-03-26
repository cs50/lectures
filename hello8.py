# Demonstrates defining a main function

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("hello,", to)

if __name__ == "__main__":
    main()

# Prints positional arguments


def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

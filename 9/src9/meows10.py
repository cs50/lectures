# Uses Sphinx docstring format


def meow(n):
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise ValueError: If n is invalid
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")

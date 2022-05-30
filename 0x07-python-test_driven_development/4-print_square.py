#!/usr/bin/python3
"""

the print "4-square_module" module.
prints a square with the character #


"""


def print_square(size):
    """
    prints a square with the character

    Args:
        size: prints character #

    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

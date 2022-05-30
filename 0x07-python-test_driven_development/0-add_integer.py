#!/usr/bin/python3
"""

the "0-add_integer" module.

"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
    a (int, float): add the first int
    b (int, float): add the second int
    return:
       (int): result sum a and b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return a + b

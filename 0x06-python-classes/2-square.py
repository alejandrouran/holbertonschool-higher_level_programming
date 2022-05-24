#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """new object of class Square"""

    def __init__(self, size=0):
        """initialize Square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

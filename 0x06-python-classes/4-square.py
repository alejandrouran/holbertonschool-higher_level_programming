#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """new object of class Square"""

    def __init__(self, size=0):
        """initialize Square"""

        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

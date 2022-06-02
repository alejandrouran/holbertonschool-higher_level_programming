#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """new object of class Square"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        get  width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        get width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return perimeter of Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        print rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def ___repr__(self):
        """
        Return representation rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        print message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

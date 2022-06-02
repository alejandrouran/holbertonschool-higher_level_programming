#!/usr/bin/python3
"""


Rectangle module


"""


class Rectangle:

    """defines the class rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle class
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        set height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        print the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (('#' * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """
        Return represenation class of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

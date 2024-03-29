#!/usr/bin/python3
"""base_geometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

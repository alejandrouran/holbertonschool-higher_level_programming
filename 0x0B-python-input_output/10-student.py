#!/usr/bin/python3
"""The function student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"representation of a Student instance """
        if type(attrs) is list and all(type(y) is str for y in attrs):
            n_dict = {}
            for a in attrs:
                if a in self.__dict__:
                    n_dict[a] = self.__dict__[a]
            return n_dict
        else:
            return self.__dict__

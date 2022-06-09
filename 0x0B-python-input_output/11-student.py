#!/usr/bin/python3
"""The function student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Initialize method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"representation of a Student instance """
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for a, value in self.__dict__.items():
            if a in attrs:
                n_dict[a] = value
        return n_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for a, value in json.items():
            setattr(self, a, value)

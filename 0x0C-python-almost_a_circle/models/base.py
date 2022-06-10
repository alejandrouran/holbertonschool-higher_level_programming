#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""

import json


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, if=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

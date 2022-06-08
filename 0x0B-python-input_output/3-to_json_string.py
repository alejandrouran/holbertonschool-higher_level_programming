#!/usr/bin/python3
"""the function to_json_string"""
from json import dumps


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return dumps(my_obj)




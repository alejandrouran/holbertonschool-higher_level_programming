#!/usr/bin/python3
"""The function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

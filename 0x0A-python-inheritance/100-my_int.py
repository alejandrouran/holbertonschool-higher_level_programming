#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """
    ...
    """
    def __eq__(self, x):
        """eq"""
        return not super().__eq__(x)

    def __ne__(self, x):
        """
        ...
        """
        return not super().__ne__(x)

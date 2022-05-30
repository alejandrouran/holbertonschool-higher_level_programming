#!/usr/bin/python3
"""

the "2-matrix_divided" module


"""


def matrix_divided(matrix, div):
    """
    Function divides a matrix
    """
    if type(matrix) is not list:
        raise TypeError("listError")
    for i in range(len(matrix)):
        if i is not 0:
            result = i - 1
            if len(matrix[i]) is not len(matrix[result]):
                raise TypeError("sizeError")
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div is 0:
        raise TypeError('division by zero')

    return [[round(i / div, 2) for i in m_list] for m_list in matrix]

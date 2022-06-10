#!/usr/bin/python3
"""The function pascal_triangle"""


def pascal_triangle(n):

    if n <= 0:
        return ""

    triangle = [[1]]
    for i in range(1, n):
        x = [1]
        j = triangle[i - 1]
        for e in range(1, i):
            x.append(j[e] + j[e - 1])
        x.append(1)
        triangle.append(x)
    return triangle

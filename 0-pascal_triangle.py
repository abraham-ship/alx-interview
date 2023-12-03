#!/usr/bin/python3

'''this module prints the pascal's triangle'''


def pascal_triangle(n):
    '''print pascal's triangle'''
    triangle = []

    for i in range(n):
        # loop to get leading spaces
        row = [1] * (i + 1)

        # loop to get elements of row i
        for j in range(1, i):
            row[j] = triangle[j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

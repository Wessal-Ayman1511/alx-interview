#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]
    # Build the triangle row by row
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Add the values between the first and last element of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)
    return triangle

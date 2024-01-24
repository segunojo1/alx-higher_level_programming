#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in i:
            return j**2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

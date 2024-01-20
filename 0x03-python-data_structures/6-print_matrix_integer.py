#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lis in matrix:
            for lis2 in lis:
                print("{:d}".format(lis2), end=" ")
            print('')

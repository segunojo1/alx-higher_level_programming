#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            print("{:s}".format(""))
        else:
            for lis in matrix:
                for lis2 in lis:
                    print("{:d}".format(lis2), end=" ")
                print('')

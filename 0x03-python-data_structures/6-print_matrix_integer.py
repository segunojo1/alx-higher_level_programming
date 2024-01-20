#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            print("{:s}".format(""))
        else:
            for lis in matrix:
                for lis2 in range(0, len(lis)):
                    if lis2 < len(lis) - 1:
                        print("{:d}".format(lis[lis2]), end=" ")
                    else:
                        print("{:d}".format(lis[lis2]))

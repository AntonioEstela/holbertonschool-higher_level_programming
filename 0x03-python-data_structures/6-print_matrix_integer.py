#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 1
        for j in i:
            print("{:d}".format(j), end="")
            if len(i) > k:
                print(end=" ")
            k += 1
        print(end="\n")

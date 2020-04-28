#!/usr/bin/python3
for first in range(10):
    for second in range((first + 1), 10):
        if first != 8 and second > first:
            print("{:d}{:d}, ".format(first, second), end="")
        elif first == 8 and second == 9:
            print("{1:d}{0:d}".format(second, first))

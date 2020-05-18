#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = 0
    w = 0
    for i in my_list:
        s += i[0] * i[1]
        w += i[1]
    return s / w

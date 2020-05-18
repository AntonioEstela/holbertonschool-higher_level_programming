#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            elements += 1
        except:
            break
    print("")
    return elements

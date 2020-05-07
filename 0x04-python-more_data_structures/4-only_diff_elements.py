#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for element in set_1:
        if element not in set_2:
            new.append(element)
    for element2 in set_2:
        if element2 not in set_1:
            new.append(element2)
    return new

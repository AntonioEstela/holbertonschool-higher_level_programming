#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for pos in range(len(my_list)):
        if new_list[pos] == search:
            new_list[pos] = replace
    return new_list

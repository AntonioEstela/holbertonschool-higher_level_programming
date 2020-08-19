#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function to find a Peak"""
    if not list_of_integers:
        return None
    peak = find(list_of_integers, 0, len(list_of_integers) - 1,
                len(list_of_integers))
    return peak


def find(lst, low, high, maxi):
    """function to find a Peak"""
    check = low + (high - low)/2
    check = int(check)

    if (check == 0 or lst[check - 1] <= lst[check]) and\
       (check == maxi - 1 or lst[check + 1] <= lst[check]):
        return lst[check]

    elif (check > 0 and lst[check + 1] > lst[check]):
        return find(lst, check + 1, high, maxi)
    else:
        return find(lst, low, check - 1, maxi)

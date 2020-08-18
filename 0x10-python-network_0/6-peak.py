#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers."""

    if list_of_integers == []:
        return None

    peak = 0

    for i in list_of_integers:
        if i > peak:
            peak = i

    return peak

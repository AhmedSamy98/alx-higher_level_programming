#!/usr/bin/python3
"""
    This is a peak module
    Author: Peter Ekwere

"""


def isPeak(a_list, size, number, index_i, index_j):
    """ This function returns true if peak else false
    """
    if index_i is not None and a_list[index_i] > number:
        return False

    if index_j is not None and a_list[index_i] > number:
        return False

    return True


def find_peak(list_of_integers):
    """ This function returns the peak in a list
    """
    if not list_of_integers:
        return

    size = len(list_of_integers)
    index_j = size - 1
    new_list = []
    for index_i in range(1, len(list_of_integers)):
        number = list_of_integers[index_i]
        if isPeak(list_of_integers, size, number, index_i, index_j):
            new_list.append(number)
    peak = max(new_list)
    return peak

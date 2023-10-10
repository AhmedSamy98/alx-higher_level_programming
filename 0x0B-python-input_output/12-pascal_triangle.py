#!/usr/bin/python3
"""
    Module: pascal_triangle
"""


def pascal_triangle(n):
    """
        Returns a Pascal's triangle
        list of n.

            Args:
                n (int): An integer
    """
    result = []
    prev = []
    curr = []
    curr_len = 0

    while n > 0:
        prev = curr
        curr = curr + [1]
        i = 1
        while i < len(prev):
            curr[i] = prev[i - 1] + prev[i]
            i += 1
        result.append(curr)
        n -= 1

    return result

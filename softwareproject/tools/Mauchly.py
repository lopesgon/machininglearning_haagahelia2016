#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
This module provides a method to sort instances faster than the usual QuickSort algorithm.
"""

def getPosition(lst, c):
    """
    Goes through the array using dichotomy principle to find the position where the new object
    as to be inserted in.
    Pre-required: the array as to be already sorted!
    :param lst: an array of instances of c
    :param c: an object
    :return: index as an int
    """
    pos = 0
    n = len(lst)-1
    if n <= 0 or c < lst[0]:
        pos = 0
    elif c >= lst[n]:
        pos = n+1
    else:
        g = 0
        d = n
        while g < d - 1:
            m = int((g + d) / 2)
            if c >= lst[m]:
                g = m
            else:
                d = m
        pos = d
    return pos
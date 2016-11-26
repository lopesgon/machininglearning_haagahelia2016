#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def getPosition(lst, c):
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
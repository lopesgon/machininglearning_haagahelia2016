#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Mauchly(object):

    @staticmethod
    def getPosition(lst, c):
        pos = 0
        n = len(lst) - 1
        if len(lst) == 0:
            return 0
        if c < lst[0]:
            return 0
        elif c >= lst[n]:
            pos = n + 1
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
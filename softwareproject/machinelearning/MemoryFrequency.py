#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class MemoryFrequency(object):

    def __init__(self, indice, frequency):
        self._indice = indice
        self._frequency = frequency

    @property
    def indice(self):
        return self._indice

    @property
    def frequency(self):
        return self._frequency

    def __str__(self):
        return str(self.indice) + " " + str(self.frequency)

    def _repr_(self):
        return self.__str__()

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.indice == other.indice

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __le__(self, other):
        return self.frequency <= other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency
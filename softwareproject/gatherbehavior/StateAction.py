#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from softwareproject.tools.ComparableTime import ComparableTime

class StateAction(object):
    global DATE_FORMAT
    global TIME_FORMAT
    DATE_FORMAT = '%d.%m.%Y %H:%M:%S'
    TIME_FORMAT = '%H:%M:%S'

    def __init__(self, type, date, frequency):
        self._type = type
        self._date = date
        self._frequency = int(frequency)

    @property
    def typeAction(self):
        return self._type

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self.date.strftime(TIME_FORMAT)

    @property
    def frequency(self):
        return self._frequency

    def comparaisonDateTime(self,date2):
        return ComparableTime.CompareDateWithTime(self.date,date2)

    def __str__(self):
        return self.date.strftime(DATE_FORMAT) + " " + " Frequency = " + str(self.frequency)

    def _repr_(self):
        return self.__str__()

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.date == other.date

    def __lt__(self, other):
        result = self.comparaisonDateTime(other.date)
        result = ComparableTime.CompareDateWithTime(self.date,other.date)
        return result == -1

    def __gt__(self, other):
        result = self.comparaisonDateTime(other.date)
        return result == 1

    def __le__(self, other):
        result = self.comparaisonDateTime(other.date)
        return result == -1 or result == 0

    def __ge__(self, other):
        result = self.comparaisonDateTime(other.date)
        return result == 1 or result == 0


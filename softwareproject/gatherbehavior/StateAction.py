#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.tools.TimeTools import CompareDateWithTime

"""
StateAction class contains all the data regarding to an action with an IndoorItem.
"""

class StateAction(object):
    global DATE_FORMAT
    global TIME_FORMAT
    DATE_FORMAT = '%d.%m.%Y %H:%M:%S'
    TIME_FORMAT = '%H:%M:%S'

    def __init__(self, type, date, frequency):
        """
        Constructor of StateAction class
        :param type: boolean
        :param date: datetime
        :param frequency: int
        """
        self._type = type
        self._date = date
        self._frequency = int(frequency)

    @property
    def typeAction(self):
        """
        :return: boolean
        """
        return self._type

    @property
    def date(self):
        """
        :return: datetime
        """
        return self._date

    @property
    def time(self):
        """
        :return: time as a String
        """
        return self.date.strftime(TIME_FORMAT)

    @property
    def frequency(self):
        """
        :return: frequency as a int
        """
        return self._frequency

    def comparaisonDateTime(self,date2):
        """
        Compares the current datetime instance value with a new one received in parameter.
        :param date2: datetime
        :return: int
        """
        return CompareDateWithTime(self.date,date2)

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
        result = CompareDateWithTime(self.date,other.date)
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


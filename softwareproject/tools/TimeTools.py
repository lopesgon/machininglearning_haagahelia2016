#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime
"""
This module provides methods to manage Time.
"""
def getHours():
    """
    Add new table in lstHours.
    Add 96 tables
    :return: array
    """
    lstHours = []
    for i in range(0,96):
        hour = []
        lstHours.append(hour)
    return lstHours

def getTimeFromSeconds(seconds):
    """
    Converts seconds into format HH:MM:SS with a static date 2016/11/11
    :param seconds: seconds as int
    :return: a datetime instance
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return datetime.datetime(2016,11,11,int(h),int(m),int(s))

def getSecondsFromTime(d):
    """
    Converts a datetime time into seconds without taking care of the date.
    :param d: datetime
    :return: int
    """
    sumSec = int(0)
    sumSec += (d.hour * 3600)
    sumSec += (d.minute * 60)
    sumSec += (d.second)
    return sumSec

def CompareDateWithTime(date1,date2):
    """
    Provides a compareTo() solution to compare two times.
    :param date1: datetime
    :param date2: datetime
    :return:
    """
    if date1.hour > date2.hour:
        return 1
    elif date1.hour < date2.hour:
        return -1
    elif date1.minute > date2.minute:
        return 1
    elif date1.minute < date2.minute:
        return -1
    elif date1.second > date2.second:
        return 1
    elif date1.second < date2.second:
        return -1
    else:
        return 0
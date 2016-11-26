#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Parameter: date1
Parameter: date2
Return: 1 if date1 is bigger, -1 if date2 is bigger, 0 if the the are the same
"""
def CompareDateWithTime(date1,date2):
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
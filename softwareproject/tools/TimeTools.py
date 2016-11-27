#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime

#Parameter: lstHours --> an array for storing other table
#Action: add new table in lstHours
#Nb table added: 48
def getHours():
    lstHours = []
    for i in range(0,96):
        hour = []
        lstHours.append(hour)
    return lstHours


# Parameter: seconds
# Parameter Type: int
# Action: convert seconds into format HH:MM:SS
# Return a date from the seconds
def getTimeFromSeconds(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    # Date Static - to improve
    return datetime.datetime(2016,11,11,int(h),int(m),int(s))

def getSecondsFromTime(d):
    sumSec = int(0)
    sumSec += (d.hour * 3600)
    sumSec += (d.minute * 60)
    sumSec += (d.second)
    return sumSec

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
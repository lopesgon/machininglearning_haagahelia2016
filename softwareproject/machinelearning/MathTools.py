#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.tools import TimeTools
"""
This module provides many mathematic calculation for the time slots algorithm generator.
"""
def calculateAverageActions(tabActions):
    """
    Go through a list of StateAction and return the average time of all instances in the array in seconds
    :param tabActions: array of StateAction
    :return: average as int
    """
    sumSec = int(0)
    sumFrequency = int(0)
    for act in tabActions:
        frequency = int(act.frequency)
        sumFrequency = int(sumFrequency) + frequency
        d = act.date
        sumSec = sumSec + (d.hour * 3600) * frequency
        sumSec = sumSec + (d.minute * 60) * frequency
        sumSec = sumSec + (d.second) * frequency
    return sumSec / sumFrequency

def calculateMedian(tabActions):
    """
    Calculate the median of an array of StateAction.
    :param tabActions: array of StateAction
    :return: datetime
    """
    frec = int(0)
    nbFrec = float((getFrequency(tabActions)+1)/2)
    for i in range(0,len(tabActions)):
        action = tabActions[i]
        if frec + action.frequency == nbFrec:
            return tabActions[i].date
        elif frec + action.frequency > nbFrec: # the next one will be bigger than nbFrec
            seconds = 0
            if frec + 1 > nbFrec: #we have to do the average between tabAction[i-1] and tabAction[i]
                seconds = getAverageBetweenTwoTimes(tabActions[i-1],tabActions[i])
                return TimeTools.getTimeFromSeconds(seconds)
            else:#the two number making the border are in tabActions[i]
                return tabActions[i].date
        else:
            frec = frec + action.frequency
    return None

def getAverageBetweenTwoTimes(time1,time2):
    """
    Calculate the average time between two times and returns it in seconds representation
    :param time1: datetime
    :param time2: datetime
    :return: average in seconds as a int
    """
    d1 = time1.date
    d2 = time2.date
    sumSec = 0
    sumSec = sumSec + (d1.hour+d2.hour) * 3600
    sumSec = sumSec + (d1.minute+d2.minute) * 60
    sumSec = sumSec + (d1.second + d2.second)
    return sumSec/2

def getFrequency(lstStateAction):
    """
    Go through the array and sum the frequency of each action frequency
    :param lstStateAction: array of StateAction
    :return: frequency as a int
    """
    f = int(0)
    for act in lstStateAction:
        f = f + act.frequency
    return int(f)

def getFrequencyFromMemories(lstMemories):
    """
    Go through the array and sum the frequency of each memory
    :param lstMemories: array of MemoryFrequency
    :return: frequency as a int
    """
    f = int(0)
    for mem in lstMemories:
        f = f + mem.frequency
    return int(f)

def getCumulativeFrequency(tabMemoryFreq, sumFrequency):
    """
    This method return the cumulative frequency from a list of instances of MemoryFrequency and the sum of the frequency received
    in parameter.
    :param tabMemoryFreq: array of MemoryFrequency instances
    :param sumFrequency: sum as a int of all frequencies
    :return: index of the highest frequency
    """
    fCum = tabMemoryFreq[len(tabMemoryFreq)-1].frequency / sumFrequency
    ind = len(tabMemoryFreq)-2
    while ind >= 0 and fCum <= 0.5:
        fCum = fCum + tabMemoryFreq[ind].frequency / sumFrequency
        ind = ind -1
    return ind
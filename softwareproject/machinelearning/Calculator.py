#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.gatherbehavior.MemoryFrequency import MemoryFrequency
from softwareproject.gatherbehavior.StateAction import StateAction
from softwareproject.machinelearning import MathTools
from softwareproject.tools import Mauchly
from softwareproject.tools import TimeTools

"""
This module is providing the algorithm which generates suitable Time slots for an IndoorItem instance
regarding to the ON/OFF StateAction events of it.
"""

def generateSuitableTimes(item, lstStateActions):
    """
    Generate and return a list of ON time slots
    :param item: instance of an IndoorItem
    :param lstStateActions:
    :return:
    """
    if len(lstStateActions)>0:
        #Create the tree and place the StateActions in the right leaf
        lstHours = _manageAction(lstStateActions)
        lstMemories = _getLstMemories(item, lstHours)
        frequency = MathTools.getFrequencyFromMemories(lstMemories)
        firstRelevantInd = MathTools.getCumulativeFrequency(lstMemories, frequency)+1
        resDataOn = _getLstTimeResult(lstMemories[firstRelevantInd:],lstHours)
        item.setResDataOn(resDataOn)
        lstHoursOff = _manageAction(item.dataOff)
        lstMemoriesOff = _getLstMemories(item, lstHoursOff)
        resDataOff = _generateSuiteableTimesOff(resDataOn,lstHoursOff,lstMemoriesOff)
        item.setResDataOff(resDataOff)
    else:
         print("No StateAction instance in " + item.name + "!")


def _generateSuiteableTimesOff(resDataOn,lstHoursOff,lstMemoriesOff):
    size = len(resDataOn)-1
    i = 0
    lstResOff = []
    while i < size:
        act = _getSuitableTime(resDataOn[i],resDataOn[i+1],lstHoursOff,lstMemoriesOff)
        if act is None:
            del resDataOn[i+1]
            size = size - 1
        else:
            lstResOff.append(act)
            i = i + 1
    act = _getSuitableTimeBetweenMaxAndMin(resDataOn[-1], resDataOn[0], lstHoursOff, lstMemoriesOff)
    if act is not None:
        lstResOff.append(act)
    return lstResOff

def _getSuitableTime(lAction,rAction,lstHoursOff,lstMemoriesOff):
    for mem in reversed(lstMemoriesOff):
        lst = lstHoursOff[mem.indice]
        d = MathTools.calculateMedian(lst)
        if d is None:
            return None
        act = StateAction("false",d,1)
        if lAction <= act and act < rAction:
            return act
    return None

def _getSuitableTimeBetweenMaxAndMin(lAction,rAction,lstHoursOff,lstMemoriesOff):
    for mem in reversed(lstMemoriesOff):
        lst = lstHoursOff[mem.indice]
        d = MathTools.calculateMedian(lst)
        if d is None:
            return None
        act = StateAction("false", d, 1)
        if lAction <= act or act < rAction:
            return act
    return None

def _manageAction(lstStateActions):
    """
    Go through the different StateAction instances and insert them inside a tree
    :param lstStateActions: array of StateAction
    :return: array
    """
    lstHours = TimeTools.getHours()
    for act in lstStateActions:
        d = act.date
        if d.minute >= 45:
            lstHours[act.date.hour * 4 + 3].append(act)
        elif d.minute >= 30:
            lstHours[act.date.hour * 4 + 2].append(act)
        elif d.minute >= 15:
            lstHours[act.date.hour*4+1].append(act)
        else:
            lstHours[act.date.hour*4].append(act)
    return lstHours

def _getLstMemories(item, lstHours):
    """
    Shows the different time slots generated for the tree received in parameter
    :param item: instance of IndoorItem
    :param lstHours: tree of all StateAction instances
    :return:
    """
    sumFrequency = int(0)
    tabMemoryFreq = []
    for i in range(0,len(lstHours)):
        f = MathTools.getFrequency(lstHours[i])
        memory = MemoryFrequency(i,f)
        ind = Mauchly.getPosition(tabMemoryFreq,memory)
        tabMemoryFreq.insert(ind,memory)
        sumFrequency = sumFrequency + f
    return tabMemoryFreq


def _getLstTimeResult(tabMemoryFreq,lstHours):
    """

    :param tabMemoryFreq: array
    :param lstHours: array
    :return: array with suitable StateAction made of the suitable time
    """
    tabRes = []
    for mem in tabMemoryFreq:
        #Two next lines are for an average
        #nbSeconds = MathTools.calculateAverageActions(lstHours[mem.indice])
        #TimeTools.getTimeFromSeconds(nbSeconds)
        d = MathTools.calculateMedian(lstHours[mem.indice])
        if d is not None:
            action = StateAction("true",d,1)
            ind = Mauchly.getPosition(tabRes,action)
            tabRes.insert(ind,action)
    return tabRes
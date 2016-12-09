#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.gatherbehavior.IndoorItem import *
from softwareproject.gatherbehavior.StateAction import *
from softwareproject.tools import StrTo
from datetime import datetime

#DATA_ACTIONS = "dataAction.csv"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

"""
This Data Access Object (DAO) module is in charge of creating instances of StateAction for each ON/OFF event.
"""
def getOffActions(item):
    """
    Returns an array with the OFF StateAction instances of the item in parameter
    :param item: instance of IndoorItem
    :return: array of OFF StateAction
   """
    return _getActionsItem(item.fileDataOff)


def getOnActions(item):
    """
    Returns an array with the ON StateAction instances of the item in parameter
    :param item: instance of IndoorItem
    :return: array of ON StateAction
    """
    return _getActionsItem(item.fileDataOn)

def _getActionsItem(fileName):
    """
    It reads the fileName and add the instances of StateAction into the instance of IndoorItem
    :param fileName: a .csv file name available in the ressources folder

    """
    data=[]
    try:
        fichier = open(fileName, "r")
        actions = fichier.read()
        tab = actions.splitlines()
        for actionLine in tab:
            action = _readActionLine(actionLine)
            pos = Mauchly.getPosition(data, action)
            data.insert(pos, action)
    except Exception:
        print("The file " + fileName + " does not exist!")
    return data

def _readActionLine(actionLine):
    """
    Receives the data of a StateAction instance as a String and creates an instance of StateAction.
    :param actionLine: a comma-separated string containing data of an StateAction instance
    :return: an instance of StateAction
    """
    lstFeatures = actionLine.split(";")
    actionType = StrTo.strToBool(lstFeatures[1])
    date = date_object = datetime.strptime(lstFeatures[2], DATE_FORMAT)
    frequency = lstFeatures[3]
    action = StateAction(actionType, date, frequency)
    return action
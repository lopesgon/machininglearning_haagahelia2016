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

def readAllActions(item):
    """
    Fills int the IndoorItem instance with the StateAction ON/OFF instances regarding to the .csv file
    stored into the instance.
    :param item: instance of IndoorItem
    :return:
    """
    fillItemWithAction(item,item.fileDataOn)
    fillItemWithAction(item, item.fileDataOff)

def fillItemWithAction(item,fileName):
    """
    It reads the fileName and add the instances of StateAction into the instance of IndoorItem
    :param item: instance of IndoorItem
    :param fileName: a .csv file

    """
    try:
        # read the file
        fichier = open(fileName, "r")
        actions = fichier.read()
        # spread the line in a table
        tab = actions.splitlines()
        # manage a line
        for actionLine in tab:
            # create a State Action
            action = _readActionLine(actionLine)
            # Affect the action to the object
            item._addAction(action)
    except Exception:
        print("The file " + fileName + " does not exist!")

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
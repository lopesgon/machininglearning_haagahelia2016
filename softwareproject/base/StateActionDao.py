#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.gatherbehavior.IndoorItem import *
from softwareproject.gatherbehavior.StateAction import *
from softwareproject.tools import StrTo
from datetime import datetime

#DATA_ACTIONS = "dataAction.csv"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


"""
@:param: Item
Action: fill the Item with StateActionON
Action: fill the Item with StateActionOff
"""
def readAllActions(item):
    fillItemWithAction(item,item.fileDataOn)
    fillItemWithAction(item, item.fileDataOff)

"""
Parameter: item
Paramete: fileName
Action: read the fileName and add the StateAction in the item
"""
def fillItemWithAction(item,fileName):
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


#Parameter: actionLine
#Return: Action
def _readActionLine(actionLine):
    lstFeatures = actionLine.split(";")
    actionType = StrTo.strToBool(lstFeatures[1])
    date = date_object = datetime.strptime(lstFeatures[2], DATE_FORMAT)
    frequency = lstFeatures[3]
    action = StateAction(actionType, date, frequency)
    return action
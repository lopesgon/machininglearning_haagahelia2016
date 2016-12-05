#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.gatherbehavior.IndoorItem import *

"""
This Data Access Object (DAO) module is in charge of creating instances of IndoorItems' and return them in an array.
"""

def readItem(dataFile):
    """
    Fills in an array with instances of IndoorItem regarding to the .csv file and returns it.
    :param dataFile: a .csv file which contains the data of an IndoorItem
    :return: an array with instances of IndoorItem
    """
    lstItems = []
    fichier = open(dataFile, "r")
    items = fichier.read()
    tab = items.splitlines()
    for lineItem in tab:
        item = __readLine(lineItem)
        if item not in lstItems:
            lstItems.append(item)
    fichier.close()
    return lstItems

def __readLine(lineItem):
    """
    Receives a String comma-separated with data of an IndoorItem.
    :param lineItem: String comma-separated containing an IndoorItem instance information
    :return: an instance of IndoorItem
    """
    lstFeatures = lineItem.split(";")
    no = lstFeatures[0]
    name = lstFeatures[1]
    fileDataOn = lstFeatures[2]
    fileDataOff = lstFeatures[3]
    indItem = IndoorItem(no, name,fileDataOn,fileDataOff, [], [])
    return indItem
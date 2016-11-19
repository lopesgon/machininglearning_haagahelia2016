#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Software Engineering Project
#Machining Learning - Gathering behaviour in an indoor environment
#Frédéric Lopes Gonçalves Magalhaes (a1602054) & Nicolas Delbiaggio (a1602052)
#2016-2017, semester 5

from datetime import datetime
from softwareproject.tools.StrTo import StrTo
from softwareproject.base.StateActionDao import StateActionDao
from softwareproject.base.ItemDao import ItemDao
from softwareproject.machinelearning.Calculator import Calculator

if __name__ == "__main__":
    ITEMS_FILE = "dataItems.csv"
    DATA_ACTIONS = "dataAction.csv"
    lstItems = []

    #Load Items in a list
    print("LOADING INDOOR ITEMS...")
    ItemDao.readItem(lstItems, ITEMS_FILE)

    #Load StateAction in Items
    print("LOADING ACTIONS OF THE ITEMS")
    for item in lstItems:
        StateActionDao.readAllActions(item)

    #Generate the suitable times and add them in the Items
    print("GENERATION OF SUITABLE TIMESLOTS PER ITEM")
    for item in lstItems:
        Calculator.generateSuitableTimes(item, item.dataOn)

    #Print the result of all suitable Times
    print("PRINTING RESULTS PHASE")
    for item in lstItems:
        StrTo.strUnderline(item.name)
        resOn = item.resDataOn
        resOff = item.resDataOff
        for i in range(len(resOn)):
            print("On  = " + str((resOn[i]).time))
            print("Off = " + str((resOff[i]).time))
        print("END ITEM: " + str(item))
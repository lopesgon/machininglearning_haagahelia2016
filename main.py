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
    ItemDao.readItem(lstItems, ITEMS_FILE)

    #Load StateAction in Items
    for item in lstItems:
        StateActionDao.readAllActions(item)
    print("====================================")
    print()

    #Generate the suitable times and add them in the Items
    for item in lstItems:
        Calculator.generateSuitableTimes(item, item.dataOn)
    print("====================================")
    print()

    #Print the result of all suitable Times
    for item in lstItems:
        print()
        StrTo.strUnderline(item.name)
        resOn = item.resDataOn
        resOff = item.resDataOff
        for i in range(len(resOn)):
            print("On  = " + str((resOn[i]).time))
            print("Off = " + str((resOff[i]).time))
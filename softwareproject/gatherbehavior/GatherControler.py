from softwareproject.base import ItemDao
from softwareproject.base import StateActionDao
from softwareproject.machinelearning import Calculator
from softwareproject.tools import StrTo
from softwareproject.base.TestingDao import writingLine
import time
import datetime

"""
This module is a controler which is in charge of managing all the items created and execute updates, gathering behavior, etc..
"""

def run():
    """
    Launch the software by creating instances and running the automation.
    """
    _runningAutomation()

def _runningAutomation():
    """
    Starts the software by executing the method start() of each IndoorItem instance.
    :param lstItems: array of IndoorItem instances
    """
    lstItems = []
    lstItems = _init(lstItems)
    while True:
        for item in lstItems:
            item.start()
        #time.sleep(3600*24*7) #WEEK STANDBY
        time.sleep(3600) #FOR TEST PURPOSE
        for item in lstItems:
            item.stop()
        writingLine("UPDATING ALL OBJECTS! System Time: " + str(datetime.datetime.today()))
        #_updateTimeSlots(lstItems)
        lstItems = _init(lstItems)

def _listeningUser(lstItems):
    """
    @deprecated NOT USED IN FINAL VERSION
    Starts the software by executing the method start() of each IndoorItem instance.
    Opens an input dialog in terminal to allow the user to interact with the software.
    :param lstItems: array of IndoorItem instances
    """
    etat = True
    while etat != "exit":
        if etat == "start":
            for item in lstItems:
                item.start()
        elif etat == "stop":
            stopAllProcesses(lstItems)
        elif etat == "update":
            print("UPDATE TIMESLOTS")
            _updateTimeSlots(lstItems)
        else:
            print("ERROR: input '" + etat + "' incorrect! Please write one of the specific words asked for.")
        etat = input("Write 'start/stop/update/exit' to interact with the process: ")
    stopAllProcesses(lstItems)

def stopAllProcesses(lstItems):
    """
    @deprecated NOT USED IN FINAL VERSION
    Stops all the automation process of each IndoorItem instance.
    :param lstItems: array of IndoorItem instances
    """
    for item in lstItems:
        item.stop()

def _updateTimeSlots(lstItems):
    """
    @deprecated NOT USED IN FINAL VERSION
    Generates the suitable times and add them in the Items.
    :param lstItems: array of IndoorItem instances
    """
    writingLine("GENERATE SUITABLE TIMESLOTS PER ITEM. System time: " + str(datetime.datetime.today()))
    for item in lstItems:
        Calculator.generateSuitableTimes(item) #, item.dataOn) #OLD VERSION IN COMMENT

def _init(lstItems):
    """
    Initialisation of the software by creating instance of IndoorItem and generating the first TimeSlots of them.
    :param lstItems: array of IndoorItem instances
    :return: an array with the IndoorItem instances with their timeslots generated
    """
    ITEMS_FILE = "dataItems.csv"
    DATA_ACTIONS = "dataAction.csv"

    #Load Items in a list
    writingLine("LOADING INDOOR ITEMS. System time: " + str(datetime.datetime.today()))
    lstItems = ItemDao.readItem(ITEMS_FILE)

    #Load StateAction in Items
    writingLine("LOADING ACTIONS PER ITEM. System time: " + str(datetime.datetime.today()))
    for item in lstItems:
        StateActionDao.readAllActions(item)

    _updateTimeSlots(lstItems)

    #PRINT THE RESULT OF ALL SUITABLE TIMESLOTS GENERATED
    # print("PRINTING RESULTS PHASE")
    # for item in lstItems:
    #     StrTo.strUnderline(item.name)
    #     resOn = item.resDataOn
    #     resOff = item.resDataOff
    #     for i in range(len(resOn)):
    #         print("On  = " + str((resOn[i]).time))
    #         print("Off = " + str((resOff[i]).time))
    #     print("END ITEM: " + str(item))

    return lstItems
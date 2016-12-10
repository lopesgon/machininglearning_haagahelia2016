from softwareproject.base import ItemDao
from softwareproject.base import StateActionDao
from softwareproject.machinelearning import Calculator
from softwareproject.tools import StrTo
from softwareproject.base.LogDao import writingLine
import time
import datetime

"""
This module is a controler which is in charge of managing all the items created and execute updates, gathering behavior, etc..
"""
fileItems = "dataItems.csv"
def run():
    """
    Launch the software by creating instances and running the automation.
    """
    writingLine("\n\nSoftware Engineering Project - SOFTWARE TURNING ON TIME : " + str(datetime.datetime.today()))
    _runningAutomation()
    writingLine("\nSOFTWARE TURNING OFF TIME: " + str(datetime.datetime.today()))

def _runningAutomation():
    """
    Starts the software by executing the method start() of each IndoorItem instance.
    :param lstItems: array of IndoorItem instances
    """
    lstItems = _init(fileItems)
    while True:
        time.sleep(3600*24*7+3600*2) #more than 1 week in case of problems, the items will be updated.
        writingLine("\nWEEKLY UPDATE OF THE OBJECTS AUTOMATION(each hour for testing)! System Time: " + str(datetime.datetime.today()))
        _updateActions(lstItems)
        _updateTimeSlots(lstItems)

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
            _stopAllProcesses(lstItems)
        elif etat == "update":
            print("UPDATE TIMESLOTS")
            _updateTimeSlots(lstItems)
        else:
            print("ERROR: input '" + etat + "' incorrect! Please write one of the specific words asked for.")
        etat = input("Write 'start/stop/update/exit' to interact with the process: ")
    _stopAllProcesses(lstItems)

def _stopAllProcesses(lstItems):
    """
    Stops all the automation process of each IndoorItem instance.
    :param lstItems: array of IndoorItem instances
    """
    for item in lstItems:
        item.stop()

def _runAllProcesses(lstItems):
    """
    Run all automation process of each instance receive in parameter
    :param lstItems: array of IndoorItem
    """
    for item in lstItems:
        item.start()

def _updateActions(lstItems):
    writingLine("\nLOADING ACTIONS PER ITEM. System time: " + str(datetime.datetime.today()))
    for item in lstItems:
        item.setDataOn(StateActionDao.getOnActions(item))
        item.setDataOff(StateActionDao.getOffActions(item))

def _updateTimeSlots(lstItems):
    """
    @deprecated NOT USED IN FINAL VERSION
    Generates the suitable times and add them in the Items.
    :param lstItems: array of IndoorItem instances
    """
    writingLine("\nGENERATE SUITABLE TIMESLOTS PER ITEM. System time: " + str(datetime.datetime.today()))
    _stopAllProcesses(lstItems)
    for item in lstItems:
        Calculator.generateSuitableTimes(item)
    _runAllProcesses(lstItems)

def _init(file):
    """
    Initialisation of the software by creating instance of IndoorItem and generating the first TimeSlots of them.
    :param file: String as file containing all items data
    :return: an array with the IndoorItem instances with their timeslots generated
    """
    ITEMS_FILE = "dataItems.csv"
    lstItems = []
    writingLine("\nLOADING INDOOR ITEMS. System time: " + str(datetime.datetime.today()))
    lstItems = ItemDao.readItem(file)
    _updateActions(lstItems)
    _updateTimeSlots(lstItems)
    #PRINT THE RESULT OF ALL SUITABLE TIMESLOTS GENERATED - FOR TESTING PURPOSE
    #_printingTimeSlotsResult(lstItems)
    return lstItems

def _printingTimeSlotsResult(lstItems):
    print("PRINTING RESULTS PHASE")
    for item in lstItems:
        StrTo.strUnderline(item.name)
        resOn = item.resDataOn
        resOff = item.resDataOff
        for i in range(len(resOn)):
            print("On  = " + str((resOn[i]).time))
            print("Off = " + str((resOff[i]).time))
        print("END ITEM: " + str(item))

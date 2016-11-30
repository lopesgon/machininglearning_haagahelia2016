from softwareproject.base import ItemDao
from softwareproject.base import StateActionDao
from softwareproject.machinelearning import Calculator
from softwareproject.tools import StrTo
import time

def run():
    lstItems = []
    lstItems = _init(lstItems)
    _runningAutomation(lstItems)
    #_listeningUser(lstItems, "start")

def _runningAutomation(lstItems):
    for item in lstItems:
        item.start()
    print("LAUNCHING PHASE: PASSED")
    while True:
        time.sleep(3600*24)

#This method was used to gather the actions that the user wanted to do NOT REQUIRED FOR FINAL VERSION
def _listeningUser(lstItems, etat):
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

#NOT REQUIRED FOR FINAL VERSION
def stopAllProcesses(lstItems):
    for item in lstItems:
        item.stop()

#NOT REQUIRED FOR FINAL VERSION
def _updateTimeSlots(lstItems):
    #Generate the suitable times and add them in the Items
    print("GENERATION OF SUITABLE TIMESLOTS PER ITEM")
    for item in lstItems:
        Calculator.generateSuitableTimes(item, item.dataOn)

def _init(lstItems):
    ITEMS_FILE = "dataItems.csv"
    DATA_ACTIONS = "dataAction.csv"

    #Load Items in a list
    print("LOADING INDOOR ITEMS...")
    ItemDao.readItem(lstItems, ITEMS_FILE)

    #Load StateAction in Items
    print("LOADING ACTIONS OF THE ITEMS")
    for item in lstItems:
        StateActionDao.readAllActions(item)

    _updateTimeSlots(lstItems)

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

    return lstItems
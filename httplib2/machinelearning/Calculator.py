import pandas as pd
import numpy as np
class Calculator(object):

    """
    Parameter: lstStateAction
    """
    @staticmethod
    def timeslotsGenerator(lstActions):
        print(len(lstActions))
        #Create the tree for the time slots
        lstHours = []
        Calculator.addHours(lstHours)
        #Place the Actions in the right place
        Calculator.manageAction(lstActions,lstHours)
        tabActions = Calculator.showFreqPerHour(lstHours)
        nbSeconds = Calculator.calculateAverageActions(tabActions)
        Calculator.getTimeFromSeconds(nbSeconds)

    #Parameter: seconds
    #Parameter Type: int
    #Action: convert seconds into format HH:MM:SS
    @staticmethod
    def getTimeFromSeconds(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print("%d:%02d:%02d" % (h, m, s))


    #Parameter: lstActions --> array with instance of StateAction
    #Return: the average time of all instance in the array in seconds
    #Return type: seconds
    @staticmethod
    def calculateAverageActions(tabActions):
        sumSec = int(0)
        sumFrequency = int(0)
        for act in tabActions:
            frequency = int(act.frequency)
            sumFrequency = int(sumFrequency) + frequency
            d = act.date
            sumSec = sumSec + (d.hour * 3600) * frequency
            sumSec = sumSec + (d.minute * 60) * frequency
            sumSec = sumSec + (d.second) * frequency
        return sumSec/sumFrequency


    #Parameter: lstStateAction --> an array with instance of stateAction
    #Parameter: lstHours --> an array with all time Slots
    #Actions: add the Action in the right place in the array lstHours
    @staticmethod
    def manageAction(lstActions,lstHours):
        for act in lstActions:
            d = act.date
            if d.minute >= 30:
                lstHours[act.date.hour*2+1].append(act)
            else:
                lstHours[act.date.hour*2].append(act)


    #Parameter: lstHours --> list of all StateAction regroupped in different array
    #Return: the lstStateAction with the biggest frequency
    #Action: go through all StateAction array and get the mod
    @staticmethod
    def showFreqPerHour(lstHours):
        ind = 0
        mod = Calculator.getFrequency(lstHours[0])
        print("Hour: " + str(0) + " Frequency: " + str(mod))
        for i in range(1,len(lstHours)):
            f = Calculator.getFrequency(lstHours[i])
            if mod < f:
                mod = f
                ind = i
            print("Hour: " + str(i) + " Frequency: " + str(f))
        print("Mod = " + str(mod) + " à l'heure  " + str(ind/2))
        return lstHours[ind]


    #Parameter: lstStateAction
    #Return: frequency
    #Action: go through the array and addition the frequency of each action.frequency
    @staticmethod
    def getFrequency(lstStateAction):
        f = int(0)
        for act in lstStateAction:
            f = f + act.frequency
        return f


    #Parameter: lstHours --> an array for storing other table
    #Action: add new table in lstHours
    #Nb table added: 48
    @staticmethod
    def addHours(lstHours):
        for i in range(0,48):
            hour = []
            lstHours.append(hour)


    def __analyzingData(self):
        None
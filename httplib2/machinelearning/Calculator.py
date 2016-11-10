import pandas as pd
import numpy as np
from httplib2.tools.MemoryFrequency import MemoryFrequency
from httplib2.tools.Mauchly import Mauchly
class Calculator(object):

    """
    Parameter: lstStateAction
    """
    @staticmethod
    def timeslotsGenerator(lstActions):
        if len(lstActions)>0:
            print(len(lstActions))
            #Create the tree for the time slots
            lstHours = []
            Calculator.addHours(lstHours)
            #Place the Actions in the right place
            Calculator.manageAction(lstActions,lstHours)


            Calculator.showFreqPerHour(lstHours)
            #nbSeconds = Calculator.calculateAverageActions(tabActions)
            #Calculator.getTimeFromSeconds(nbSeconds)
        else:
            print("Il n'y a pas de StateAction!")

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
            if d.minute >= 45:
                lstHours[act.date.hour * 4 + 3].append(act)
            elif d.minute >= 30:
                lstHours[act.date.hour * 4 + 2].append(act)
            elif d.minute >= 15:
                lstHours[act.date.hour*4+1].append(act)
            else:
                lstHours[act.date.hour*4].append(act)


    #Parameter: lstHours --> list of all StateAction regroupped in different array
    #Return: the lstStateAction with the biggest frequency
    #Action: go through all StateAction array and get the mod
    @staticmethod
    def showFreqPerHour(lstHours):
        ind = 0
        mod = Calculator.getFrequency(lstHours[0])
        sumFrequency = int(0)
        tabMemoryFreq = []

        for i in range(1,len(lstHours)):
            f = Calculator.getFrequency(lstHours[i])
            memory = MemoryFrequency(i,f)
            ind = Mauchly.getPosition(tabMemoryFreq,memory)
            tabMemoryFreq.insert(ind,memory)

            sumFrequency = sumFrequency + f

        fCum = tabMemoryFreq[len(tabMemoryFreq)-1].frequency / sumFrequency
        ind = len(tabMemoryFreq)-2
        while ind >= 0 and fCum <= 0.5:
            fCum = fCum + tabMemoryFreq[ind].frequency / sumFrequency
            ind = ind -1


        for y in range(ind+1,len(tabMemoryFreq)):
            mem = tabMemoryFreq[y]
            print("MEMORY IND")
            print(mem.indice)
            print("Frequence")
            print(mem.frequency)
            nbSeconds = Calculator.calculateAverageActions(lstHours[mem.indice])
            Calculator.getTimeFromSeconds(nbSeconds)




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
        for i in range(0,96):
            hour = []
            lstHours.append(hour)


    def __analyzingData(self):
        None
import pandas as pd
import numpy as np
class Calculator(object):

    """
    Parameter: lstStateAction
    """
    @staticmethod
    def timeslotsGenerator(lstActions):
        print(len(lstActions))
        lstHours = []
        Calculator.addHours(lstHours)
        Calculator.manageAction(lstActions,lstHours)
        tabActions = Calculator.showFreqPerHour(lstHours)
        nbSeconds = Calculator.calculateAverageActions(tabActions)
        Calculator.getTimeFromSeconds(nbSeconds)

    @staticmethod
    def getTimeFromSeconds(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print("%d:%02d:%02d" % (h, m, s))

    @staticmethod
    def calculateAverageActions(tabActions):
        t = 0
        for act in tabActions:
            d = act.date
            t = t + d.hour * 3600
            t = t + d.minute * 60
            t = t + d.second
        return t/len(tabActions)


    @staticmethod
    def manageAction(lstActions,lstHours):
        for act in lstActions:
            d = act.date
            if  d.minute >= 30:
                lstHours[act.date.hour+1].append(act)
            else:
                lstHours[act.date.hour].append(act)


    #Parameter: lstHours
    @staticmethod
    def showFreqPerHour(lstHours):
        print("lstHours = " + str(len(lstHours)))
        ind = 0
        mod = len(lstHours[0])
        print("Hour: " + str(0) + " Frequency: " + str(len(lstHours[0])))
        for i in range(1,len(lstHours)):
            f = len(lstHours[i])
            if mod < f:
                mod = f
                ind = i
            print("Hour: " + str(i) + " Frequency: " + str(f))
        print("Mod = " + str(mod) + " à l'heure  " + str(ind))
        return lstHours[ind]

    @staticmethod
    def addHours(lstHours):
        for i in range(0,24):
            hour = []
            lstHours.append(hour)


    def __analyzingData(self):
        None
from httplib2.gatherbehavior.MemoryFrequency import MemoryFrequency
from httplib2.machinelearning.MathTools import *
from httplib2.machinelearning.TimeTools import *
from httplib2.gatherbehavior.StateAction import StateAction
from httplib2.tools.Mauchly import Mauchly


class Calculator(object):

    """
    Generate and return a list of time slots
    @param lstStateActions
    """
    @staticmethod
    def generateSuitableTimes(item, lstStateActions):
        if len(lstStateActions)>0:
            #Create the tree and place the StateActions in the right leaf
            lstHours = Calculator.manageAction(lstStateActions)
            lstMemories = Calculator.getLstMemories(item, lstHours)
            frequency = MathTools.getFrequencyFromMemories(lstMemories)
            firstRelevantInd = MathTools.getCumulativeFrequency(lstMemories, frequency)+1
            resDataOn = Calculator.getLstTimeResult(lstMemories[firstRelevantInd:],lstHours)
            item.setResDataOn(resDataOn)
            lstHoursOff = Calculator.manageAction(item.dataOff)
            lstMemoriesOff = Calculator.getLstMemories(item, lstHoursOff)
            resDataOff = Calculator.generateSuiteableTimesOff(resDataOn,lstHoursOff,lstMemoriesOff)
            item.setResDataOff(resDataOff)
        else:
             print("No StateAction instance in " + item.name + "!")


    @staticmethod
    def generateSuiteableTimesOff(resDataOn,lstHoursOff,lstMemoriesOff):
        size = len(resDataOn)-1
        i = 0
        lstResOff = []
        while i < size:
            act = Calculator.getSuitableTime(resDataOn[i],resDataOn[i+1],lstHoursOff,lstMemoriesOff)
            if act is None:
                del resDataOn[i+1]
                size = size - 1
            else:
                lstResOff.append(act)
                i = i + 1
        act = Calculator.getSuitableTimeBetweenMaxAndMin(resDataOn[-1], resDataOn[0], lstHoursOff, lstMemoriesOff)
        if act is not None:
            lstResOff.append(act)
        return lstResOff

    @staticmethod
    def getSuitableTime(lAction,rAction,lstHoursOff,lstMemoriesOff):
        for mem in reversed(lstMemoriesOff):
            lst = lstHoursOff[mem.indice]
            d = MathTools.calculateMedian(lst)
            if d is None:
                return None
            act = StateAction("false",d,1)
            if lAction <= act and act < rAction:
                return act
        return None

    @staticmethod
    def getSuitableTimeBetweenMaxAndMin(lAction,rAction,lstHoursOff,lstMemoriesOff):
        for mem in reversed(lstMemoriesOff):
            lst = lstHoursOff[mem.indice]
            d = MathTools.calculateMedian(lst)
            if d is None:
                return None
            act = StateAction("false", d, 1)
            if lAction <= act or act < rAction:
                return act
        return None

    """
    Go through the different StateAction instances and insert them inside a tree
    @param lstStateActions
    @return array
    """
    @staticmethod
    def manageAction(lstStateActions):
        lstHours = TimeTools.getHours()
        for act in lstStateActions:
            d = act.date
            if d.minute >= 45:
                lstHours[act.date.hour * 4 + 3].append(act)
            elif d.minute >= 30:
                lstHours[act.date.hour * 4 + 2].append(act)
            elif d.minute >= 15:
                lstHours[act.date.hour*4+1].append(act)
            else:
                lstHours[act.date.hour*4].append(act)
        return lstHours

    """
    Shows the different time slots generated for the tree received in parameter
    @param tree of all StateAction instances
    """
    @staticmethod
    def getLstMemories(item, lstHours):
        sumFrequency = int(0)
        tabMemoryFreq = []
        for i in range(0,len(lstHours)):
            f = MathTools.getFrequency(lstHours[i])
            memory = MemoryFrequency(i,f)
            ind = Mauchly.getPosition(tabMemoryFreq,memory)
            tabMemoryFreq.insert(ind,memory)
            sumFrequency = sumFrequency + f
        return tabMemoryFreq


    """
    @:param tabMemoryFreq
    @:param lstHours
    @:return tabRes ==> array with suitable StateAction made of the suitable time
    """
    @staticmethod
    def getLstTimeResult(tabMemoryFreq,lstHours):
        tabRes = []
        for mem in tabMemoryFreq:
            #Two next lines are for an average
            #nbSeconds = MathTools.calculateAverageActions(lstHours[mem.indice])
            #TimeTools.getTimeFromSeconds(nbSeconds)
            d = MathTools.calculateMedian(lstHours[mem.indice])
            action = StateAction("true",d,1)
            ind = Mauchly.getPosition(tabRes,action)
            tabRes.insert(ind,action)
        return tabRes
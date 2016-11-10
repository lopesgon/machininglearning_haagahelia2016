from httplib2.machinelearning.TimeTools import TimeTools
class MathTools(object):

    """
    Go through a list of StateAction and return the average time of all instances in the array in seconds
    @param array of StateAction
    @return seconds
    """
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
        return sumSec / sumFrequency

    @staticmethod
    def calculateMedian(tabActions):
        #temporaire
        MathTools.showTabActions(tabActions)

        frec = int(0)
        nbFrec = float((MathTools.getFrequency(tabActions)+1)/2)
        for i in range(0,len(tabActions)):
            action = tabActions[i]
            if frec + action.frequency > nbFrec: # the next one will be bigger than nbFrec
                seconds = 0
                if frec + 1 > nbFrec: #we have to do the average between tabAction[i-1] and tabAction[i]
                    seconds = MathTools.getAverageBetweenTwoTimes(tabActions[i-1],tabActions[i])
                    print("Comparaison")
                    print(tabActions[i-1])
                    print(tabActions[i])
                    return TimeTools.getTimeFromSeconds(seconds)
                else:#the two number making the border are in tabActions[i]
                    return tabActions[i].date
            else:
                frec = frec + action.frequency

    #Temporaire
    @staticmethod
    def showTabActions(tabActions):
        for act in tabActions:
            print(act)


    """
    @:param time1
    @:param time2
    @:return the average between the two times in seconds
    """
    @staticmethod
    def getAverageBetweenTwoTimes(time1,time2):
        d1 = time1.date
        d2 = time2.date
        sumSec = 0
        sumSec = sumSec + (d1.hour+d2.hour) * 3600
        sumSec = sumSec + (d1.minute+d2.minute) * 60
        sumSec = sumSec + (d1.second + d2.second)
        return sumSec/2


    """
    Go through the array and sum the frequency of each action frequency
    @param lstStateAction
    @return frequency
    """
    @staticmethod
    def getFrequency(lstStateAction):
        f = int(0)
        for act in lstStateAction:
            f = f + act.frequency
        return int(f)

    """
    This method return the cumulative frequency from a list of instances of MemoryFrequency and the sum of the frequency received
    in parameter.
    @param tabMemoryFreq, sumFrequency
    @return int
    """
    @staticmethod
    def getCumulativeFrequency(tabMemoryFreq, sumFrequency):
        fCum = tabMemoryFreq[len(tabMemoryFreq)-1].frequency / sumFrequency
        ind = len(tabMemoryFreq)-2
        while ind >= 0 and fCum <= 0.5:
            fCum = fCum + tabMemoryFreq[ind].frequency / sumFrequency
            ind = ind -1
        return fCum
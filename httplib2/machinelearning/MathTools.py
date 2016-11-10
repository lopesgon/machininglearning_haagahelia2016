
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
        return sumSec/sumFrequency

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
        return f

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
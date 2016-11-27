import threading
import datetime
import time
from softwareproject.tools import TimeTools
from softwareproject.gatherbehavior.IndoorItem import *
from softwareproject.base.TestingDao import writingLine

class ThreadTime(threading.Thread):

    def __init__(self, item):
        threading.Thread.__init__(self)
        self.etat = True
        self._item = item
        self._indNext = self._indNextEvent(self._item.resDataOn)

    def run(self):
        self._running()

    def _running(self):
        while self.etat:
            writingLine(str(self._item) + " falling asleep till turning ON time:" + self._item.resDataOn[self._indNext].time + "\n")
            self._sleeping(self._item.resDataOn, self._indNext)
            writingLine("TURN ON! Waking up now! System Time: " + datetime.datetime.today() + " -- ")
            writingLine(str(self._item) + "Falling asleep till turning OFF time:" + self._item.resDataOff[self._indNext].time + "\n")
            self._sleeping(self._item.resDataOff, self._indNext)
            writingLine("System Time when waking up: " + datetime.datetime.today() + "\n")
            writingLine(str(self._item) + " turn OFF!" + "\n")
            self._indNext += 1
            if self._indNext > len(self._item.resDataOff)-1:
                self._indNext = 0

    def stop(self):
        etat =  False

    def _indNextEvent(self, dates):
        d = datetime.datetime.today()
        ind = 0
        while ind <= len(dates)-1 and TimeTools.CompareDateWithTime(dates[ind].date, d) < 1:
            ind += 1
        if ind > len(dates)-1:
            return 0
        return ind

    def _sleeping(self, dates, ind):
        d = datetime.datetime.today()
        timeSleeping = TimeTools.getSecondsFromTime(dates[ind].date) - TimeTools.getSecondsFromTime(d)
        if timeSleeping < 0:
            timeSleeping = TimeTools.getSecondsFromTime(datetime.datetime(1970, 1, 1, int(23), int(59), int(59)))
            timeSleeping -= timeSleeping - TimeTools.getSecondsFromTime(d)
            timeSleeping += TimeTools.getSecondsFromTime(dates[ind].date)
        time.sleep(timeSleeping)
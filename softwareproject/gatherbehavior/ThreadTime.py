import threading
import datetime
import time
from softwareproject.tools import TimeTools
from softwareproject.gatherbehavior.IndoorItem import *
from softwareproject.base.TestingDao import writingLine

"""
ThreadTime class extends threading.Thread and is an independent process in the software.
It will allow each instance to behave in its own independently from the main process.
"""

class ThreadTime(threading.Thread):

    def __init__(self, item):
        """
        Constructor
        :param item: IndoorItem instance
        """
        threading.Thread.__init__(self)
        self._etat = True
        self._item = item
        self._indNext = self._indNextEvent(self._item.resDataOn)

    def run(self):
        """
        Public method used to run the thread.
        """
        self._running()

    def _running(self):
        """
        Run a continuous process which will set off the ON/OFF events of the IndoorItem known.
        """
        while self._etat:
            self._sleeping(self._item.resDataOn, self._indNext)
            writingLine("\n" + str(self._item) + " TURN ON! System Time: " + str(datetime.datetime.today()) + "\n")
            self._sleeping(self._item.resDataOff, self._indNext)
            if(not self._etat):
                break
            writingLine("\n" + str(self._item) + " TURN OFF! System Time: " + str(datetime.datetime.today()) + "\n")
            self._indNext += 1
            if self._indNext > len(self._item.resDataOff)-1:
                self._indNext = 0

    def stop(self):
        """
        Stops the process by changing the value of the loop condition to False
        """
        self._etat =  False

    def kill(self):
        """
        Kills the Thread by destroying the relation with its owner instance (IndoorItem instance).
        """
        self.stop()
        self._item = None

    def _indNextEvent(self, dates):
        """
        Find and return the index of the next time that has to be set off.
        :param dates: array of StateAction
        :return: index as int
        """
        d = datetime.datetime.today()
        ind = 0
        while ind <= len(dates)-1 and TimeTools.CompareDateWithTime(dates[ind].date, d) < 1:
            ind += 1
        if ind > len(dates)-1:
            return 0
        return ind

    def _sleeping(self, dates, ind):
        """
        This method will stop the thread process during a determine time calculated in
        seconds till the next event of the array in parameter.
        :param dates: array of StateAction
        :param ind: index as int
        """
        d = datetime.datetime.today()
        timeSleeping = TimeTools.getSecondsFromTime(dates[ind].date) - TimeTools.getSecondsFromTime(d)
        if timeSleeping < 0:
            timeSleeping = TimeTools.getSecondsFromTime(datetime.datetime(1970, 1, 1, int(23), int(59), int(59)))
            timeSleeping -= TimeTools.getSecondsFromTime(d)
            timeSleeping += TimeTools.getSecondsFromTime(dates[ind].date)
        time.sleep(timeSleeping)
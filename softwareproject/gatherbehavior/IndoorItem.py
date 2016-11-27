#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
class Item:
    An Item could be any furniture in an indoor environment. It is composed of:
        an No: that helps the system to distinguish each one
        a Name: in order to know which kind of object it is
        TimeSlotsStateAction: an array of StateAction defining the time slots of the object
        DataTurnOn: an array of StateAction recording each interaction with the current instance for 7 days
        DataTurnOff: an array of StateAction recording each interaction with the current instance for 7 days
"""

from softwareproject.tools import Mauchly
from softwareproject.gatherbehavior.ThreadTime import *

class IndoorItem(object):

    def __init__(self, no, name,fileDataOn,fileDataOff, dataOn, dataOff):
        self._no = no
        self._name = name
        self._fileDataOn = fileDataOn
        self._fileDataOff = fileDataOff
        self._dataOn = dataOn
        self._dataOff = dataOff
        self._resDataOn = []
        self._resDataOff = []
        self.t = None

    @property
    def no(self):
        return self._no

    @property
    def name(self):
        return self._name

    @property
    def fileDataOn(self):
        return self._fileDataOn

    @property
    def fileDataOff(self):
        return self._fileDataOff

    @property
    def dataOn(self):
        return self._dataOn

    @property
    def dataOff(self):
        return self._dataOff

    @property
    def resDataOn(self):
        return self._resDataOn

    @property
    def resDataOff(self):
        return self._resDataOff

    def setResDataOn(self,data):
        self._resDataOn = data

    def setResDataOff(self,data):
        self._resDataOff = data

    def _addResDataOn(self, data):
        pos = Mauchly.getPosition(self.resDataOn, data)
        self.resDataOn.insert(pos, data)

    def _addResDataOff(self, data):
        pos = Mauchly.getPosition(self.resDataOff, data)
        self.resDataOff.insert(pos, data)

    def _addDataOn(self, data):
        pos = Mauchly.getPosition(self.dataOn, data)
        self.dataOn.insert(pos, data)

    def _addDataOff(self, data):
        pos = Mauchly.getPosition(self.dataOff, data)
        self.dataOff.insert(pos, data)
        # self.dataOff.append(data)

    def _addAction(self, action):
        if action.typeAction:
            self._addDataOn(action)
        else:
            self._addDataOff(action)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return self.no == other.no

    def __str__(self):
        st = self.no + " " + self.name
        # st += "\n   Time ON"
        # for action in self.dataOn:
        #     st += " - "
        #     st += str(action)
        # st += "\n   Time Off"
        # for action in self.dataOff:
        #     st += " - "
        #     st += str(action)
        return st

    def _repr_(self):
        return self.__str__()

    def start(self):
        print(self)
        print(" /!\ STARTING /!\ ")
        self._listening(True)

    def stop(self):
        print(self)
        print(" /!\ STOP /!\ ")
        self._listening(False)

    def _listening(self, etat):
        if etat:
            if self.t is not None:
                self.t.stop()
                t = None
            t = ThreadTime(self)#, self._resDataOn, self._resDataOff)
            t.start()
        else:
            if self.t is not None:
                self.t.stop()
                self.t = None
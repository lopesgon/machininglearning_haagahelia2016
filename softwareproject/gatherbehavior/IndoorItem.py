#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from softwareproject.tools import Mauchly
from softwareproject.gatherbehavior.ThreadTime import *

class IndoorItem(object):

    """
    class Item
        An Item could be any furniture in an indoor environment. It is composed of:
            No: that helps the system to distinguish each one
            Name: in order to know which kind of object it is
            TimeSlotsStateAction: an array of StateAction defining the time slots of the object
            DataTurnOn: an array of StateAction recording each interaction with the current instance for 7 days
            DataTurnOff: an array of StateAction recording each interaction with the current instance for 7 days
    """

    def __init__(self, no, name,fileDataOn,fileDataOff, dataOn, dataOff):
        """
        Build an instance of IndoorItem by receiving the next parameters.
        :param no: primary key
        :param name: description of the indoor item
        :param fileDataOn: a .csv file name to import and export StateActions' related to ON events
        :param fileDataOff: a .csv file name to import and export StateActions' related to OFF events
        :param dataOn: an array containing of instances of StateAction of the ON events
        :param dataOff: an array containing of instances of StateAction of the OFF events
        """
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
        """
        Property of an IndoorItem.
        :return: primary key as a int
        """
        return self._no

    @property
    def name(self):
        """
        Property of an IndoorItem describing the object.
        :return: description as a String
        """
        return self._name

    @property
    def fileDataOn(self):
        """
        Property of an IndoorItem
        :return: a .csv file name as a String
        """
        return self._fileDataOn

    @property
    def fileDataOff(self):
        """
        Property of an IndoorItem
        :return: a .csv file name as a String
        """
        return self._fileDataOff

    @property
    def dataOn(self):
        """
        Property of an IndoorItem representing the ON events of the instance
        :return: array of ON StateAction instances
        """
        return self._dataOn

    @property
    def dataOff(self):
        """
        Property of an IndoorItem representing the OFF events of the instance
        :return: array of OFF StateAction instances
        """
        return self._dataOff

    @property
    def resDataOn(self):
        """
        Property of an IndoorItem representing the ON timeslots events generated.
        :return: array of ON events as StateAction instances
        """
        return self._resDataOn

    @property
    def resDataOff(self):
        """
        Property of an IndoorItem representing the OFF timeslots events generated.
        :return: array of OFF events as StateAction instances
        """
        return self._resDataOff

    def setResDataOn(self,data):
        """
        Sets the Timeslots for the ON events of the IndoorItem instance
        :param data: an array of StateAction instances
        """
        self._resDataOn = data

    def setResDataOff(self,data):
        """
        Sets the Timeslots for the OFF events of the IndoorItem instance
        :param data: an array of StateAction instances
        """
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
        """
        Start the independent process of the IndoorItem instance.
        """
        print(self)
        print(" /!\ STARTING /!\ ")
        self._listening(True)

    def stop(self):
        """
        Stop the independent process of the IndoorItem instance.
        """
        print(self)
        print(" /!\ STOP /!\ ")
        self._listening(False)

    def _listening(self, etat):
        """
        Creates or kills the ThreadTime instance created that is in charge of the automation of the object regarding
        to the timeslots of it.
        :param etat: boolean
        """
        if etat:
            if self.t is not None:
                self.t.stop()
                t = None
            t = ThreadTime(self)
            t.start()
        else:
            if self.t is not None:
                self.t.stop()
                self.t = None
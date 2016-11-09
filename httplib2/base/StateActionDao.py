from httplib2.gatherbehavior.IndoorItem import *
from httplib2.gatherbehavior.StateAction import *
from httplib2.tools import StrTo
from datetime import datetime

#DATA_ACTIONS = "dataAction.csv"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

class StateActionDao(object):

    @staticmethod
    def readAction(lstItems, data_actions):
        fichier = open(data_actions, "r")
        items = fichier.read()
        tab = items.splitlines()
        for actionLine in tab:
            itemNumber = actionLine.split(";")[0]
            ind = lstItems.index(IndoorItem(itemNumber, "", [], []))
            item = lstItems[ind]
            action = StateActionDao._readActionLine(actionLine)
            item._addAction(action)

    @staticmethod
    def _readActionLine(actionLine):
        lstFeatures = actionLine.split(";")
        actionType = StrTo.strToBool(lstFeatures[1])
        date = date_object = datetime.strptime(lstFeatures[2], DATE_FORMAT)
        frequency = lstFeatures[3]
        action = StateAction(actionType, date, frequency)
        return action
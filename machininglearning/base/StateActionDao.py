from machininglearning.gatherbehavior import StateAction
from machininglearning.gatherbehavior import Item
from machininglearning.tools import strTo
from datetime import datetime

DATA_ACTIONS = "dataAction.csv"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

@staticmethod
def readAction(lstItems):
    fichier = open(DATA_ACTIONS, "r")
    items = fichier.read()
    tab = items.splitlines()
    for actionLine in tab:
        itemNumber = actionLine.split(";")[0]
        ind = lstItems.index(Item(itemNumber, ""))
        item = lstItems[ind]
        action = _readActionLine(actionLine)
        item._addAction(action)

@staticmethod
def _readActionLine(actionLine):
    lstFeatures = actionLine.split(";")
    actionType = strToBool(lstFeatures[1])
    date = date_object = datetime.strptime(lstFeatures[2], DATE_FORMAT)
    frequency = lstFeatures[3]
    action = StateAction(actionType, date, frequency)
    return action
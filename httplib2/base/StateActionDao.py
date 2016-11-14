from httplib2.gatherbehavior.IndoorItem import *
from httplib2.gatherbehavior.StateAction import *
from httplib2.tools.StrTo import StrTo
from datetime import datetime

#DATA_ACTIONS = "dataAction.csv"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

class StateActionDao(object):

    """
    @:param: Item
    Action: fill the Item with StateActionON
    Action: fill the Item with StateActionOff
    """
    @staticmethod
    def readAllActions(item):
        StateActionDao.fillItemWithAction(item,item.fileDataOn)
        StateActionDao.fillItemWithAction(item, item.fileDataOff)


    """
    Parameter: item
    Paramete: fileName
    Action: read the fileName and add the StateAction in the item
    """
    @staticmethod
    def fillItemWithAction(item,fileName):
        try:
            # read the file
            fichier = open(fileName, "r")
            actions = fichier.read()
            # spread the line in a table
            tab = actions.splitlines()
            # manage a line
            for actionLine in tab:
                # create a State Action
                action = StateActionDao._readActionLine(actionLine)
                # Affect the action to the object
                item._addAction(action)
        except FileNotFoundError:
            print("The file " + fileName + " does not exist!")


    #Parameter: actionLine
    #Return: Action
    @staticmethod
    def _readActionLine(actionLine):
        lstFeatures = actionLine.split(";")
        actionType = StrTo.strToBool(lstFeatures[1])
        date = date_object = datetime.strptime(lstFeatures[2], DATE_FORMAT)
        frequency = lstFeatures[3]
        action = StateAction(actionType, date, frequency)
        return action
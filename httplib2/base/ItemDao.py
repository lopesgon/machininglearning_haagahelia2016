from httplib2.gatherbehavior.IndoorItem import *

class ItemDao(object):

    @staticmethod
    def readItem(lstItems, dataFile):
        fichier = open(dataFile, "r")
        items = fichier.read()
        tab = items.splitlines()
        for lineItem in tab:
            item = ItemDao.__readLine(lineItem)
            if item not in lstItems:
                lstItems.append(item)
                print(item.name)
        fichier.close()

    @staticmethod
    def __readLine(lineItem):
        lstFeatures = lineItem.split(";")
        no = lstFeatures[0]
        name = lstFeatures[1]
        indItem = IndoorItem(no, name, [], [])
        return indItem
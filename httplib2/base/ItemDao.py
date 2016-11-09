from httplib2.gatherbehavior.IndoorItem import IndoorItem

#global data = "dataItems.csv"

class ItemDao(object):

    @staticmethod
    def readItem(data):
        global lstItems
        lstItems = []
        fichier = open(data, "r")
        items = fichier.read()
        tab = items.splitlines()
        for lineItem in tab:
            item = ItemDao._readLine(lineItem)
            if item not in lstItems:
                lstItems.append(item)
                print(item.name)
        fichier.close()

    @staticmethod
    def _readLine(lineItem):
        lstFeatures = lineItem.split(";")
        no = lstFeatures[0]
        name = lstFeatures[1]
        return IndoorItem(no, name)
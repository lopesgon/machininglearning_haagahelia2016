from machininglearning.gatherbehavior import Item

DATA_ITEM = "dataItems.csv"

class ItemDao:

    @staticmethod
    def readItem():
        global lstItems
        lstItems = []
        fichier = open(DATA_ITEM, "r")
        items = fichier.read()
        tab = items.splitlines()
        for lineItem in tab:
            item = _readLine(lineItem)
            if item not in lstItems:
                lstItems.append(item)
                print(item.name)
        fichier.close()

def _readLine(lineItem):
    lstFeatures = lineItem.split(";")
    no = lstFeatures[0]
    name = lstFeatures[1]
    return Item(no, name)
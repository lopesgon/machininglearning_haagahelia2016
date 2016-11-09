
# print("The software is on. Please wait a minute, the computer is analyzing all data stored.")

#Software Engineering Project
#Machining Learning - Gathering behaviour in an indoor environment
#Frédéric Lopes Gonçalves Magalhaes (a1602054) & Nicolas Delbiaggio (a1602052)
#2016-2017, semester 5
from httplib2.tools.StrTo import StrTo
from httplib2.base.StateActionDao import StateActionDao
from httplib2.base.ItemDao import ItemDao


class Main:

    if __name__ == "__main__":
        # lstPers = _readFile()
        # _mainMenu(lstPers)
        global FILENAME
        FILENAME = "dataItems.csv"

        global lstItems
        lstItems = []
        StrTo.strUnderline("Items Loading")
        ItemDao.readItem(FILENAME)
        StrTo.strUnderline("Action Loading")
        print("\n")
        lstItems
        StateActionDao.readAction(lstItems)
        StrTo.strUnderline("List of Items with their Data")
        for item in lstItems:
            print(item)
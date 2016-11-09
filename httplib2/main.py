
# print("The software is on. Please wait a minute, the computer is analyzing all data stored.")

#Software Engineering Project
#Machining Learning - Gathering behaviour in an indoor environment
#Frédéric Lopes Gonçalves Magalhaes (a1602054) & Nicolas Delbiaggio (a1602052)
#2016-2017, semester 5
from httplib2.tools.StrTo import StrTo
from httplib2.base.StateActionDao import StateActionDao
from httplib2.base.ItemDao import ItemDao

if __name__ == "__main__":
    ITEMS_FILE = "dataItems.csv"
    DATA_ACTIONS = "dataAction.csv"
    lstItems = []
    StrTo.strUnderline("Items Loading")
    ItemDao.readItem(lstItems, ITEMS_FILE)
    StrTo.strUnderline("Action Loading")
    print("\n")
    StateActionDao.readAction(lstItems, DATA_ACTIONS)
    StrTo.strUnderline("List of Items with their Data")
    for item in lstItems:
        print(item)
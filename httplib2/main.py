
# print("The software is on. Please wait a minute, the computer is analyzing all data stored.")

#Software Engineering Project
#Machining Learning - Gathering behaviour in an indoor environment
#Frédéric Lopes Gonçalves Magalhaes (a1602054) & Nicolas Delbiaggio (a1602052)
#2016-2017, semester 5
from datetime import datetime

from httplib2.tools.StrTo import StrTo
from httplib2.base.StateActionDao import StateActionDao
from httplib2.base.ItemDao import ItemDao
from httplib2.tools.ComparableTime import ComparableTime

if __name__ == "__main__":
    ITEMS_FILE = "dataItems.csv"
    DATA_ACTIONS = "dataAction.csv"
    lstItems = []
    StrTo.strUnderline("Items Loading")

    #Charger les items
    ItemDao.readItem(lstItems, ITEMS_FILE)

    StrTo.strUnderline("Action Loading")
    print("\n")

    #Charger les actions dans les items
    for item in lstItems:
        StateActionDao.readAllActions(item)


    StrTo.strUnderline("List of Items with their Data")


    for item in lstItems:
        print(item)

    StrTo.strUnderline("Data Comparaison - Date complète ")

    DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

    d1 = datetime.strptime("07.10.2016 10:10:00", DATE_FORMAT)
    d2 = datetime.strptime("08.10.2016 10:10:10", DATE_FORMAT)
    if d1 > d2 :
        print("D1 " + str(d1))
    else:
        print("D2 " + str(d2))



    ##################################################################

    StrTo.strUnderline("Data Comparaison - time")

    result = ComparableTime.CompareDateWithTime(d1,d2)
    if result == 1:
        print(d1 )
    elif result == -1:
        print(d2)
    else:
        print("Equals")


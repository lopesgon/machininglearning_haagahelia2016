#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime
class TimeTools(object):

    #Parameter: lstHours --> an array for storing other table
    #Action: add new table in lstHours
    #Nb table added: 48
    @staticmethod
    def getHours():
        lstHours = []
        for i in range(0,96):
            hour = []
            lstHours.append(hour)
        return lstHours


    # Parameter: seconds
    # Parameter Type: int
    # Action: convert seconds into format HH:MM:SS
    # Return a date from the seconds
    @staticmethod
    def getTimeFromSeconds(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return datetime.datetime(2016,11,11,int(h),int(m),int(s))
        #Time static - We have to modify it
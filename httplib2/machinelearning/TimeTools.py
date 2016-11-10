
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
    @staticmethod
    def getTimeFromSeconds(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print("%d:%02d:%02d" % (h, m, s))
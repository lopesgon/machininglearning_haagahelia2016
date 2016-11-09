from datetime import datetime

class StateAction:
    global DATE_FORMAT
    DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

    def __init__(self, type, date, frequency):
        self._type = type
        self._date = date
        self._frequency = frequency

    @property
    def typeAction(self):
        return self._type

    @property
    def date(self):
        return self._date

    @property
    def frequency(self):
        return self._frequency

    def __str__(self):
        return self.date.strftime(DATE_FORMAT)

    def _repr_(self):
        return self.__str__()

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return other.date < self.date

    def __le__(self, other):
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__eq__(other):
            return True
        if self.__gt__(other):
            return True
        else:
            return False
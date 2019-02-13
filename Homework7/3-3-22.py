import datetime
import calendar

class Date:
    def __init__(self,year,month,date):
        self._year = year
        self._month = month
        self._date = date

    def dayOfWeek(self):
        week = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
        q = self._date
        m = self._month

        k = self._year %100

        if m == 1:
            m = 13
            k = k-1
        elif m == 2:
            m = 14
            k = k -1
        j = self._year // 100
        h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j)%7
        return week[h]

    def daysBetween(self,other):
        day1 = datetime.date(self._year,self._month,self._date)
        day2 = datetime.date(other._year,other._month,other._date)
        return (day1-day2).days

today = Date(2019,2,7)

print(today.dayOfWeek())
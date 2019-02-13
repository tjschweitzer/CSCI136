class oneTime:
    def __init__(self,hours,mins,seconds):
        self._totalSeconds = (hours * 3600) + (mins*60)+seconds

    def __str__(self):
        sec = self._totalSeconds % 60
        mins = int((self._totalSeconds - sec)/60) %60
        hours = int(self._totalSeconds / 3600)
        return f"Hours {hours} Minutes {mins} Seconds {sec}"

class Time:
    def __init__(self,hours,mins,seconds):
        self._hour = hours
        self._min = mins
        self._sec = seconds
    def __str__(self):

        return f"Hours {self._hour} Minutes {self._min} Seconds {self._sec}"


times = oneTime(12,2,3)

print("One Var Saved ",times)

times = Time(12,2,3)

print("Three Var Saved ",times)


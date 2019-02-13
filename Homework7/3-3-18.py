class Statsfast:
    def __init__(self,a):
        self._size = len(a)
        self._sum = sum(a)
        self._sqSum = sum(((i - self._sum/self._size)**2) for i in a)

    def setSize(self):
        return self._size

    def mean(self):
        return self._sum/self._size

    def variance(self):
        return self._sqSum/self._size


class StatsSlow:
    def __init__(self,a):
        self._set = a

    def setSize(self):
        return len(self._set)

    def mean(self):
        return sum(self._set)/len(self._set)

    def variance(self):
        mean = sum(self._set)/len(self._set)

        return sum((i -mean)**2 for i in self._set)/len(self._set)



floatySet = set([1.1,2.2,3.3,4.4,5.5,6.6,.7,.888,95,1.6])

stFast = Statsfast(floatySet)

print("Fast Mean",stFast.mean())
print("Fast Set Size",stFast.setSize())
print("Fast Varaince",stFast.variance())


stslow = StatsSlow(floatySet)

print("Slow Mean",stslow.mean())
print("Slow Set Size",stslow.setSize())
print("Slow Varaince",stslow.variance())



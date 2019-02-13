class Point():
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def distanceTo(self,other):
        return ((self._y-other._y)**2+(self._x-other._x)**2)**.5

    def __str__(self):
        return "(" + str(self._x) + " , " + str(self._y) + ")"

    
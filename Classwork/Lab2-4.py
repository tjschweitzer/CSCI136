import math
class Triangle():
    def __init__(self,x,y,r):
        self._x = x
        self._y = y
        self._r = r

    def inside(self,xP,yP):
        if (math.sqrt((self._x-xP)**2+(self._y-yP)**2))<=self._r:
            return True
        return False

def sum(a):
    if len(a) == 1:
        return a[0]
    return a[0]+ sum(a[1:])

def even(a):
    if a == []:
        return 0
    if a[0]%2==0:
        return  a[0]+even(a[1:])
    return even(a[1:])


arrayL=[1,2,3,4,5,6,7,8,9]
print(sum(arrayL))
print(even(arrayL))

print(arrayL[::2])
print(arrayL[::-2])
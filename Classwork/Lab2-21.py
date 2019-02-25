class counter:
    def __init__(self):
        self._numbah = 0
    def count(self):
        self._numbah = self._numbah + 1
    def get(self):
        return self._numbah



##  Returns all positive arrays
def posArr(a,new=[]):
    if a == []:
        return new
    if a[0]>0:
        new.append(a[0])
    return posArr(a[1:],new)

def posArr2(a):
    if a == []:
        return
    if a[0]>0:
        return  [a[0]]+posArr2(a[1:])
    return posArr2(a[1:])

x = [1,2,-3,4,-5,6,-7,8]

print(posArr(x))
print(posArr2(x))
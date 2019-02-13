
## Sets can
def addSet  (a):
    newSet = set()
    for i in a:
        newSet.add(i)


def recSet(a,setty):
    if len(a) == 0:
        return setty
    return a[1:], setty.add(a[0])


class interval:
    def __int__ (self,a,b):
        self._start = a
        self._end = b

    def contains(self, item):
        if item >= self._start and item <= self._end:
            return True
        return False


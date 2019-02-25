import sys
 ## Main Handler
class stdinHandler:
    def line(self,l):
        pass
    def done(self,):
        pass
 ## Cat
class cat(stdinHandler):
    def line(self,l):
        print(l)
    def done(self):
        pass

 ## Head
class head(stdinHandler):
    def __init__(self,length):
        self._length = int(length)
        self._count = 0

    def line(self,l):
        if self._length >+ self._count:
            print(l)
        self._count = self._count + 1

    def done(self):
        pass

 ## Tail
class tail(stdinHandler):
    def __init__(self, length):
        self._length = int(length)
        self._lines = []

    def line(self, l):
        self._lines.append(l)

    def done(self):
        backArray = self._lines[::-1]
        backArray = backArray[:self._length]
        backArray = backArray[::-1]
        for i in backArray:
            print(i)

 # Sort
class sort(stdinHandler):
    def __init__(self):
        self._lines = []

    def line(self, l):
        self._lines.append(l)

    def done(self):
        sArray = self._lines
        sArray.sort()
        for i in sArray:
            print(i)

 ##Unique
class unique(stdinHandler):
    def __init__(self):
        self._lines = set()

    def line(self, l):
        self._lines.add(l)

    def done(self):
        for i in self._lines:
            print(i)

## Count
class count(stdinHandler):
    def __init__(self):
        self._lines = {}

    def line(self, l):
        if l.strip() in self._lines:
            self._lines[l] = self._lines[l] + 1
        else:
            self._lines[l] = 1

    def done(self):
        for key in self._lines:
            print(f"{key} : {self._lines[key]}")



if sys.argv[1] == "cat":
   funtion = cat()
elif sys.argv[1] == "head":
    funtion = head(sys.argv[2])
elif sys.argv[1] == "tail":
    funtion = tail(sys.argv[2])
elif sys.argv[1] == "sort":
    funtion = sort()
elif sys.argv[1] == "unique":
    funtion = unique()
elif sys.argv[1] == "count":
    funtion = count()

for l in sys.stdin:
    funtion.line(l.strip())
funtion.done()


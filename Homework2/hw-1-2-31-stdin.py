import sys

arrayList= []
for line in sys.stdin:
    line= int(line)
    arrayList.append(line)
arrayList.sort()
for i in arrayList:
    print(i)

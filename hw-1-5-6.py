import sys

arrayList= []
for line in sys.stdin:
    line= int(line)
    arrayList.append(line)
pNum=arrayList[0]

for i in range(0,len(arrayList)):
    if pNum!=arrayList[i]:
        print(pNum, end=' ')
    pNum=arrayList[i]
print(pNum)



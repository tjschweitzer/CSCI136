import sys

arrayList= []
for line in sys.stdin:
    line= int(line)
    arrayList.append(line)

print(min(arrayList))
print(max(arrayList))
print(sum(arrayList)/len(arrayList))
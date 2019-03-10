# stacks and ques
import time
s = [3,27,164,8]
v=s[-1]
del(s[-1])
print(s,v)

start= time.time()
for i in range(10000):
    s=[1]+s
end = time.time()
print (end-start)

start= time.time()
for i in range(10000):
    s.append(1)
end = time.time()
print (end-start)

# stack Last in last out
# queue
[1]
[3,1]
[7,3,1]

# stack
#     push
#         list-.>None


# Graphs
# Edges
# Vertices

def binarySearch(alist, item):
    print(alist)
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            return binarySearch(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 12, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
start = time.time()
bubbleSort(alist)
print(alist)
end = time.time()
print (end-start)
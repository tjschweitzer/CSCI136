import time
import random

def mapArray(a):
    mappy = {}
    maxNum = 0
    maxKey = ''
    start = time.time()
    for key in a:
        if key in mappy:
            mappy[key] =mappy[key]+1
        else:
            mappy[key] = 1
    for k,v in mappy.items():
        if v>maxNum:
            maxNum=v
            maxKey=k
    print(maxKey)

    end= time.time()
    print(f"Time for map counter is {end-start} for {len(a)} items")


def sortArray(a):

    start = time.time()
    a.sort()
    maxNum = 0
    currNum=a[0]
    currCount=0
    maxKey = 0
    for item in a:
        if item == currNum:
            currCount =currCount+ 1
        else:
            if currCount>maxNum:
                print(maxKey,maxNum)
                maxNum=currCount
                maxKey=item
            currCount=1
            currNum=item
    print(maxNum,maxKey)
    end= time.time()
    print(f"Time for map counter is {start-end} for {len(a)} items")

randomArr =[]
for i in range(10000):
    randomArr.append(random.randint(1,100))

mapArray(randomArr)
sortArray(randomArr)
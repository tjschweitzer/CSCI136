import sys

def checkSum(checkVal):
    newSum=0
    checkStr = str(checkVal*2)
    for j in checkStr:
        newSum+=int(j)
    return newSum


startingStr = sys.argv[1]
sum = 0
for i in range(len(startingStr)):
    if i % 2: # if even will return True, odd will return false
        sum+=checkSum(int(startingStr[i]))
    else:
        sum+=int(startingStr[i])
checkVal = 10- sum%10
finalVal=startingStr+str(checkVal)
print(finalVal)
import sys

def classy(arrayNon,n):
    for i in range (0,len(arrayNon),n):
        print (arrayNon[i])

def negAr(oldArray):
    newArray = []
    for i in oldArray:
        if i<0:
            newArray.append(i)
    return newArray


def interweave(a,b):
    newArray=[]
    for i in range(len(a)):
        newArray.append(a[i])
        newArray.append(b[i])
    return newArray


def palRec(myPal):
    if len(myPal)==1:
        return True
    elif myPal[0]==myPal[-1]:
        print(myPal[0], myPal[-1])
        palRec(myPal[1:-1])
    else:
        return False


print(palRec("tacocat"))


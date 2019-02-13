def sumInt(initalArray):
    return recurrInt(0,initalArray)


def recurrInt(sum,intArray):
    if len(intArray)==1:
        return (intArray[0]+sum)
    else:
        return recurrInt(sum+intArray[0],intArray[1:])


startingArray = [1,2,3,4,5,6,7,8,9]
print(sumInt(startingArray))
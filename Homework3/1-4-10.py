def compose(oldArray):
    newArray=[]
    for i in range(len(oldArray[1])):
        newLine=[]
        for j in  range(len(oldArray)):
            newLine.append(oldArray[j][i])
        newArray.append(newLine)
    return newArray

#test code
#a=[[1,1],[2,2],[3,3]]
#print(compose(a))

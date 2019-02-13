def recurrChar(oldString,lastRemoved='',numRemoved=0):
    if len(oldString)==1:
        if numRemoved==0:
            return oldString
        else:
            return  oldString+str(numRemoved+1)
    elif oldString[0]==oldString[1]:
        numRemoved +=1
        #print(numRemoved,oldString[1])
        return recurrChar(oldString[1:],oldString[1],numRemoved)
    else:
        if numRemoved==0:
            return oldString[0] + recurrChar(oldString[1:])
        else:
            return oldString[0]+ str(numRemoved+1) + recurrChar(oldString[1:])

ollll="qqqwwwwwwqqdfghjj"
print(recurrChar(ollll))
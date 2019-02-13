def recurrChar(oldString):
    if len(oldString)==1:
        return oldString
    elif oldString[0]==oldString[1]:
        return recurrChar(oldString[1:])
    else:
        return oldString[0] + recurrChar(oldString[1:])

ollll="qqqwwwwwwqqdfghj"
print(recurrChar(ollll))
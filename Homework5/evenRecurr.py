def recurEve(oldArray):
    if len(oldArray)==0:
        return''
    elif oldArray[0]%2==0:
        return str(oldArray[0]) + recurEve(oldArray[1:])
    else:
        return recurEve(oldArray[1:])

arrrr = [1,2,3,4,5,6,7,8,9]

print(recurEve(arrrr))
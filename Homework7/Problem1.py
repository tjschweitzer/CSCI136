def stringy(a,b):
    if a == []:
        return b
    if len(a[0]) < len(b) or len(b) == 0:
        b=a[0]
    return stringy(a[1:],b)


oldString =['','','123456','asd','sadfg']
newString = ''
print(stringy(oldString,newString))
import sys

listArray = []
for line in sys.stdin:
    listArray.append(line.strip())

if sys.argv[1] == "cat":
    for i in listArray:
        print(i)

elif sys.argv[1] == "head":
    listLen = int(sys.argv[2])
    for i in range(listLen):
        print(listArray[i])

elif sys.argv[1] == "tail":
    listLen = int(sys.argv[2])
    for i in range(len(listArray)-listLen,len(listArray)):
        print(listArray[i])

elif sys.argv[1] == "sort":
    listArray.sort()
    for line in listArray:
        print(line)

elif sys.argv[1] == "unique":
    setty = set()
    for i in listArray:
        setty.add(i)
    for i in setty:
        print(i)

elif sys.argv[1] == "count":
    dict = {}
    for i in listArray:
        if i in dict.keys():
            dict[i] =dict[i]+1
        else:
            dict[i] = 1
    for key in dict:
        print(f"{key} : {dict[key]}")

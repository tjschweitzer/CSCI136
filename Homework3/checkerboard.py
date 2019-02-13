import sys

#inputNum= int(sys.argv[1])

inputNum=5
star = '* '
for i in range(inputNum):
    if i % 2:
        print(star*inputNum)
    else:
        print('',star*(inputNum-1))
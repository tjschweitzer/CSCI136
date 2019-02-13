def printTF (boolArray):
    for line in boolArray:
        for item in line:
            if item:
                print("*",end='')
            else:
                print(' ',end='')
        print('')

# commented put test code
#startArray = [[True,False,True,True],[True,False,True,True],[True,False,True,True]]
#printTF(startArray)
##Returns length of array
def len2(arry):
    if len(arry)==1:
        return 1
    return 1 + len2(arry[1:])


##Returns the largest int in an array
def maxint(arry, max=0):
    if len(arry) == 0:
        return max
    if arry[0]>max:
       max=arry[0]
    return maxint(arry[1:], max)

#Random number to calculate pi:  piR^2




x = [1,10,111,1434,1,1,1,1]


print ("Array Length",len2(x))

print ("Largest Int",maxint(x))


import sys

#read in stdin
sysArray = []
for line in sys.stdin:
    sysArray.append(line.strip())

# Checks for unique items
sysmap = {}
for i in sysArray:
    if i in sysmap.keys():
        sysmap[i]= sysmap[i] +1
    else:
        sysmap[i]=1

# Finds max number of repeated numbers
maxVal = max(sysmap.values())
three=3

# Prints bar graph
for i in range(maxVal,0,-1):
    print(f"{i:>{three}}",end='  ')
    for keys in sysmap:
        if sysmap[keys]>=i:
            print('*',end='  ')
        else:
            print(' ',end='  ')
    print('')
print('   ',end='  ')
for i in sysmap:
    print(i,end='  ')
print('')

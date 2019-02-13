import sys

number=int(sys.argv[1])
for i in range (0,number+1):
    for j in range(0,i):
        print(i,end='')
    print('')
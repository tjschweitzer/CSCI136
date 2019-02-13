import sys


arrayList = [int( sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])]

arrayList.sort()

for i in arrayList:
    print(i)
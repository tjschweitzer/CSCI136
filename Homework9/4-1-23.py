# largest array size
# Limit is between 10000x10000 and 30000x30000

import sys


n = int(sys.argv[1])
a = [None] * n
for row in range(n):
    a[row] = [None] * n
print('finished')

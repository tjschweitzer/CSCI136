import sys
import stdio
import math

number=11
for j in range (1,number+1):
    i=2**j
    stdio.write(math.log2(i))
    stdio.write('\t')
    stdio.write(i)
    stdio.write('\t')
    stdio.write(i* math.log1p(i))
    stdio.write('\t')
    stdio.write(math.pow(i,2))
    stdio.write('\t')
    stdio.write(math.pow(i,3))
    stdio.write('\t')
    stdio.write(2**i)
    stdio.writeln()
import math, random
pi_maybe = 0
for i in range(20000000):
    if math.sqrt(random.random()**2+random.random()**2) < 1: pi_maybe += 1
print(4*pi_maybe/20000000)

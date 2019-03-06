import random
from collections import defaultdict

from lecture_02_27.elapsedtime import ElapsedTime

numbers = [random.randint(0, 100) for i in range(10000)]

with ElapsedTime("counts-naive"):
    counts = {}
    for n in numbers:
        counts[n] = numbers.count(n)

with ElapsedTime("counts-dict"):
    counts = {}
    for n in numbers:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

with ElapsedTime("counts-dict-default-method"):
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 1) + 1

with ElapsedTime("counts-defaultdict"):
    counts = defaultdict(lambda: 1)
    for n in numbers:
        counts[n] += 1


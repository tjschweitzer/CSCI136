from lecture_02_27.elapsedtime import ElapsedTime

import random

num = 100000

with ElapsedTime("built in"):
    array = [random.randint(0, 1000) for _ in range(num)]
    array.sort()

with ElapsedTime("merge"):
    import merge
    array = [random.randint(0, 1000) for _ in range(num)]
    merge.sort(array)

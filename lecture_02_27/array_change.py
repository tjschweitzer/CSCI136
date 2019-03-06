from lecture_02_27.elapsedtime import ElapsedTime

num = 100000

with ElapsedTime("build-front"):
    arr = []
    for i in range(num):
        arr = [i] + arr

with ElapsedTime("build-append"):
    arr = []
    for i in range(num):
        arr.append(i)

with ElapsedTime("build-append-reverse"):
    arr = []
    for i in range(num):
        arr.append(i)

    list(reversed(arr))

with ElapsedTime("pop-start"):
    arr = []
    for i in range(num):
        arr.append(i)

    for i in range(num):
        arr.pop(0)

with ElapsedTime("pop-end"):
    arr = []
    for i in range(num):
        arr.append(i)

    for i in range(num):
        arr.pop()


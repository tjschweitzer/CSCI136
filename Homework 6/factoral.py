
def factor(n):
    listArray = []
    i = 2
    while n>1:
        if n % i == 0:
            listArray.append(i)
            n= int(n/i)
            i=2 #Resets i to 2
        else:
            i+=1 #increases i value
    return listArray



print(factor(8))
print(factor(80))
print(factor(7))
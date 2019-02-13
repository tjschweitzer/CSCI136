def odd(a,b,c):
    count = 0
    if a:
        count+=1
    if b:
        count+=1
    if c:
        count+=1
    if count%2:
        return True
    else:
        return False

#test code
#print(odd(False,False,True))
def recurString(s, x, y):
    if len(s)==0:
        return ''
    elif s[0]==x:
        return y + recurString(s[1:],x,y)
    else:
        return s[0] + recurString(s[1:],x,y)



def stringOne(s,x,y):
    return recurString(s,x,y)


print (stringOne('foo','o','z'))
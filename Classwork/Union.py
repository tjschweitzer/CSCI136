# 3/11/19
# prints all items in both sets once
def union(a,b):
    c = set()
    for item in a:
        c.add(item)
    for item in b:
        c.add(item)
    print(c)

# prints items found in both sets
def intersect(a,b):
    c=set()
    for item in a:
        if item in b:
            c.add(item)
    print(c)

one ={1,2,3,4,5}
two={3,6,5,7,8,9}
union(one,two)
intersect(one,two)
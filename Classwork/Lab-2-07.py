class Mommie():
    def Food(self):
        print ("Veggies")

class Kid(Mommie):

    def Food(self):
        print("Candy!")

def uniArray(a,b):
    if a ==[]:
        return b
    if a[0] not in b:
        b.append(a[0])
    return uniArray(a[1:],b)


##returns first odd,
def recur(a):
    if a == []:
        return
    if a[0] % 2 == 1:
        return a[0]
    return recur(a[1:])

ara =[6,4,8,6,5,4,8,6,2,7]
print("Prints First Odd Value",recur(ara))


##returns first odd,
def recurL(a):
    if a == []:
        return
    if a[-1] % 2 == 1:
        return a[-1]
    return recur(a[:-1])

print("Prints Last Odd Value",recur(ara))


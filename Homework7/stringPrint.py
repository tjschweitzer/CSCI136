class StringBuilder:
    def __init__(self,a):
        self._arrayString = [a]


    def add(self,a):
        self._arrayString.append(a)

    def __str__(self):
        return  ''.join(self._arrayString)

one = 'one'
two = 'two'
three = 'three'

new = StringBuilder(one)
new.add(two)
new.add(three)

print(str(new))
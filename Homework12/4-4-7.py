# Compute hash(x) % 5 for the single-character keys
#
# E A S Y Q U E S T I O N
#
# Draw the hash table created when the ith key in this sequence is associated with the value i, for i from 0 to 11

class node:
    def __init__(self,data):
        self._item=data
        self.next=None


# This print statement iterates though the entire linked list and prints the values
    def __str__(self):
        print(self._item, end=' ')
        if self.next is None:
            return ' '
        temp= self.next
        while temp.next is not None:
            temp=temp.next
            print(temp._item, end=' ')
        print(temp._item,end=' ')
        return ' '


    def push(self,data):
        if self.next is None:
            self.next = node(data)
            return
        temp=self.next
        while temp.next is not None:
            temp=temp.next
        temp.next=node(data)


stringy = 'EASYQUESTION'

dict = {}
for item in stringy:
    number = hash(item) %8
    if number in dict:
        dict[number].push(item)
    else:
        dict[number] = node(item)

for key in dict:
    print(key," ",dict[key])
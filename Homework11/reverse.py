# Implement a Stack class in three ways and see how they perform when the stack has many items in it (e.g. add 10,000 numbers then remove them all)
#
# Items are added and removed at the start of an array
#
# Items are added and removed at the end of an array
#
# As a linked list

import time
import resource
import sys

# NodeClass
class stackNode:
    def __init__(self, item):
        self._item = item
        self.next = None

# Stack class
class stack:
    # nothing assigned to head yet
    def __init__(self):
        self.head = None

    # pushed to top of stack
    def push(self, data):
        temp = stackNode(data)
        temp.next = self.head
        self.head = temp

    # Pops top of stack after checking if it is empty
    def pop(self):
        if self.head==None:
            print("Empty Stack")
            return None

        tempNode=self.head
        while(tempNode.next !=  None):
            slowNode=tempNode
            tempNode=tempNode.next
        slowNode.next=None
        del(tempNode)
        return slowNode



trueStack = stack()

for line in sys.stdin:
    trueStack.push(line)

printline = trueStack.pop()
while(printline != None):
    print(printline)
    printline = trueStack.pop()



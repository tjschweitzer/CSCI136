# Compose a Queue client that takes a command-line argument k writes the kth from the last string found on standard input.

import sys

class queStack:
    def __init__(self):
        self.head=None
        self.tail=None

    # pushed to end of stack
    def push(self, data):
        temp = node(data)
        if self.head==None:  #if the stack is empty it will assign the node to the head as well
            self.head=temp
            self.tail=temp
            return
        self.tail.next=temp
        self.tail=temp


    # Pops top of stack after checking if it is empty
    def pop(self):
        if self.head == None:
            print("Empty Stack")
            return

        tempNode = self.head
        self.head = self.head.next
        return tempNode._item


class node:
    def __init__(self, item):
        self._item = item  # Reference to an item.
        self.next = None  # Reference to the next _Node object


queue = queStack()
k = int(sys.argv[1])
line = str(sys.stdin)





# Pushes each charter in the string to the stack
for i in range(len(line)):
    queue.push(line[i])

# pops from the stack until kth value is reached
for i in range(k):
    last = queue.pop()
    print(f'{last} removed')

print(f'\nThe original String was \'{line}\'')

print(f'The {k}th value from the end would be {last}')


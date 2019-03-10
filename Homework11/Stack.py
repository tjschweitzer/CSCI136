# Implement a Stack class in three ways and see how they perform when the stack has many items in it (e.g. add 10,000 numbers then remove them all)
#
# Items are added and removed at the start of an array
#
# Items are added and removed at the end of an array
#
# As a linked list

import time
import resource

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
            return

        tempNode=self.head
        self.head=self.head.next
        return tempNode._item


# Makes an array
def makeArrayStack():
    stack = []
    return stack

# pushes to to 0th element in the array
def pushStart(stack, item):
    return [item] + stack
    # print(item + " pushed to stack ")

# removes from the 0th element in the array
def popStart(stack):
    if (len(stack)==0):
        print("Empty Stack Can not Pop")
        return
    return stack[1:]

# Pushes to end of the array
def pushEnd(stack, item):
    stack.append(item)
    # print(item + " pushed to stack ")

# removes last item in array
def popEnd(stack):
    if (len(stack)==0):
        print("Empty Stack Can not Pop")
        return
    return stack.pop()



arrayStack = makeArrayStack()

start = time.time()
for i in range(1000):
    arrayStack=pushStart(arrayStack, str(i))
end =time.time()
print(f"Time to add {i+1} elements from the start {end-start}")



start = time.time()
for i in range(1000):
    arrayStack=popStart(arrayStack)
end =time.time()
print(f"Time to remove {i+1} elements from the start {end-start}")


start = time.time()
for i in range(1000):
    pushEnd(arrayStack, str(i))
end =time.time()
print(f"\nTime to add {i+1} elements from the end {end-start}")

start = time.time()
for i in range(1000):
    popEnd(arrayStack)
end =time.time()
print(f"Time to remove {i+1} elements from the end {end-start}")




trueStack = stack()

start = time.time()
for i in range (1000):
    trueStack.push(i)

end =time.time()
print(f"\nTime to add {i+1} elements in stack {end-start}")
start = time.time()
for i in range (1000):
    trueStack.pop()

end =time.time()
print(f"Time to remove {i+1} elements in stack {end-start}")



print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss )

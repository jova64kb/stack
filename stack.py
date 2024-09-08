class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        item = Node(data)
        if self.top != None:
            item.next = self.top # point to old top
        self.top = item # replace top
    def pop(self):
        if self.top != None:
            data = self.top.data
            if self.top.next != None:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
    def peek(self):
        return None if self.top == None else self.top.data

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


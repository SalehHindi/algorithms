class Stack(object):
    def __init__(self):
        self.stack = [1,2]

    def __str__(self):
        return str(self.stack)

    def push(self, pushed):
        self.stack.append(pushed)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack==[]

    def size(self):
        return len(self.stack)

a=Stack()
a.push('x')
a.push('y')
a.pop()
a.push('z')
print a.peek()
class Stack(object):
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, pushed):
        self.stack.append(pushed)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

'''
# Write a program that checks if a string has correct parentheses
string = '('
start = ['(', '[', '{']
end = {'(': ')', '[': ']', '{': '}'}
par = Stack()
for c in string:
    for p in start:
        if c == p:
            par.push(p)

    if not par.is_empty():
        if c == end[par.peek()]:
            par.pop()

if par.is_empty():
    print 'Correct matching!'

else:
    print 'damn, not correct'

'''
'''
cases:
()()()
()[]{}
{(}) wrong
({[]})
{ wrong
'''

#converts decimal to binary
integer=57
binary=Stack()

while integer:
    if integer % 8:
        integer=(integer- (integer % 8))/8
        binary.push(integer % 8)

    elif not integer % 8:
        integer = integer / 8
        binary.push(1)

print binary
class Deque(object):
    def __init__(self):
        self.deque=[]

    def __str__(self):
        return str(self.deque)

    def add_front(self, item):
        self.deque.append(item)

    def add_rear(self, item):
        self.deque = [item] + self.deque

    def pop_front(self):
        if not self.is_empty():
            self.deque.pop()

    def pop_rear(self):
        if not self.is_empty():
            self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return self.deque == []

    def front(self):
        return self.deque[-1]

    def rear(self):
        return self.deque[0]

def palindrome(input):
    deque = Deque()
    flag=0
    for i in input:
        deque.add_rear(i)
    while not deque.is_empty():
        if deque.front() == deque.rear():
            deque.pop_front(); deque.pop_rear()
        else:
            flag=1
            break
    if flag:
        return False
    else:
        return True

print palindrome('hahah')

class Queue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, item):
        self.queue = [item] + self.queue
        return self.queue

    def dequeue(self):
        self.queue.pop()
        return self.queue

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def first(self):
        if not self.is_empty():
            return self.queue[-1]

line=Queue()
constant=7
alphabet='abcdefghijklmnop'
for a in alphabet:
    line.enqueue(a)

while line.size() != 1:
    print line
    for turn in range(constant):
        potato=line.first()
        line.dequeue()
        line.enqueue(potato)
    line.dequeue()

print line
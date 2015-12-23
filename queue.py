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

line=Queue()
for i in range(10):
    line.enqueue(i)

print line

for i in range(3):
    line.dequeue()

print line
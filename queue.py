class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue("1st msg")
q.enqueue("2nd msg")
q.enqueue("3rd msg")
q.enqueue("4th msg")

print(q.items)

q.dequeue()

print(q.items)

class Queue2Stacks(object):

    def __init__(self):
        self.stack0 = []
        self.stack1 = []

    def queue(self, item):
        self.stack0.insert(0, item)
        self.stack1.insert(0, item)

    def deque(self, item):
        self.stack0.pop()
        self.stack1.pop()


q = Queue2Stacks()

for i in range(5):
    q.queue(i)

for j in range(5):
    print(q.deque())
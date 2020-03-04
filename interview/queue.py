class Queue2Stacks(object):

    def __init__(self):
        self.stack0 = []
        self.stack1 = []

    def queue(self, item):
        self.stack0.append(item)

    def deque(self):
        if not self.stack1:
            while self.stack0:
                self.stack1.append(self.stack0.pop())
        return self.stack1.pop()


q = Queue2Stacks()

q.queue(1)
q.queue(2)
q.queue(3)

print(q.stack0)
q.deque()
print(q.stack1)




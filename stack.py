class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()

# Add three elements
s.push(1)
s.push("two")
s.push(True)

print(s.peek())
print(s.size())

# Remove 1 element from top
s.pop()

# Print all elements
print(s.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(0)
b = Node(1)
c = Node(2)

a.nextnode = b
b.nextnode = c

print(a.nextnode.value)

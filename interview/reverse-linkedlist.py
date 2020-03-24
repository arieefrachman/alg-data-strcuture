class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(node):
    current = node
    previous = None
    next_node = None

    while current:
        next_node = current.nextnode
        current.nextnode = previous
        previous = current
        current = next_node

    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

print("=========")
reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
# print(a.nextnode.value)

# print(a.nextnode.value)
# print(b.nextnode.value)
# print(c.nextnode.value)




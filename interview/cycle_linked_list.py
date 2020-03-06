class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def is_cycle(node):
    mark1 = node
    mark2 = node

    while mark2 is not None and mark2.nextnode is not None:

        mark1 = mark1.nextnode
        mark2 = mark2.nextnode.nextnode
        if mark2 == mark1:
            return True
    return False


a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)

# Cycle
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a

print(is_cycle(d))

# Not cycle
x = Node(0)
y = Node(1)
z = Node(2)

x.nextnode = y
y.nextnode = z

print(is_cycle(x))






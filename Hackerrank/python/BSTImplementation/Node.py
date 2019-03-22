class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        if root.data < data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)

def minValue(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data





root = Node(10)
insert(root, Node(11))
insert(root, Node(9))
insert(root, Node(12))
print minValue(root)
print 'Finished'
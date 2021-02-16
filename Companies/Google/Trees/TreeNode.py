class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        root = TreeNode(data)
    else:
        if data > root.data:
            if root.right is None:
                root.right = TreeNode(data)
            else:
                insert(root.right, data)
        else:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                insert(root.left, data)
    return root


def bfs(root):
    stack = [root]
    while stack:
        p = stack.pop(0)
        print p.data
        if p.left:
            stack.append(p.left)
        if p.right:
            stack.append(p.right)

def max_height(root):
    if root is None:
        return 0
    l = max_height(root.left)
    r = max_height(root.right)
    return 1 + max(l, r)

root = None
root = insert(root, 10)
root = insert(root, 13)
root = insert(root, 12)
bfs(root)
print max_height(root)
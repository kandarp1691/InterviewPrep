class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Method to insert a Node in the tree
def insert(root, val):
    if root is None:
        root = Node(val)
    else:
        if root.data > val:
            if root.left is None:
                root.left = Node(val)
            else:
                insert(root.left, val)
        else:
            if root.right is None:
                root.right = Node(val)
            else:
                insert(root.right, val)
    return root

#Method to search for a key in the tree
def search(root, key):
    if root is None:
        return 'No tree exists'
    if root.data == key:
        return root
    else:
        if key < root.data:
            return search(root.left, key)
        else:
            return search(root.right, key)

#Method to print the tree in Inorder Traversal fashion
def inorder(root):
    result = ''
    if root is not None:
        inorder(root.left)
        print root.data
        inorder(root.right)
    return result

#Method to find the minimum value of the Tree
def min_value(root):
    if root is None:
        return root
    while root.left is not None:
        root = root.left
    print root.data

def delete_node(root, key):
    if root is None:
        return None

    #If val to be deleted is less than root its in left subtree
    if key < root.data:
        root.left = delete_node(root.left, key)

    #If val to be deleted is greater than root, its in right subtree
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value(root.right)

        root.data = temp.data

        root.right = delete_node(root.right, temp.key)

    return root

def find_lca(root, n1, n2):
    if root is None:
        return root
    if root.data > n1 and root.data > n2:
        return find_lca(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return find_lca(root.right, n1, n2)
    return root

# Find the kth smallest node
def kthsmallest(root, k):
    if root is None:
        return root
    else:
        node = root
        stack = []
        count = 0
        while stack != [] or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                inorder_node = stack.pop()
                count += 1
                if count == k:
                    return inorder_node.data
                node = node.right
        return None

#Print a range of all values between k1 and k2
def print_range(root, k1, k2):
    if root is None:
        return root
    else:
        if k1 < root.data:
            print_range(root.left, k1, k2)
        if k1 <= root.data and k2 >= root.data:
            print root.data
        if k2 > root.data:
            print_range(root.right, k1, k2)


#Find the height of BST
def get_height(root):
    if root is None:
        return 0
    else:
        return 1 + max(get_height(root.left) , get_height(root.right))


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print 'Inorder Traversal Result is:'
inorder(root)

print 'Minimun value of the tree is'
min_value(root)

print 'Height of Tree is'
print get_height(root)
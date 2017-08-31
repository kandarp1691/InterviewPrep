class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return False
        else:
            if self.data < data:
                if self.right:
                    return self.right.insert(data)
                else:
                    self.right = Node(data)
            else:
                if self.left:
                    return  self.left.insert(data)
                else:
                    self.left = Node(data)

    def find(self, data):
        if self.data == data:
            return True
        elif self.data < data:
            if self.right:
                return self.right.find(data)
            else:
                return False
        else:
            if self.left:
                return self.left.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print str(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print str(self.data)

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print str(self.data)
            if self.right:
                self.right.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print "Pre-Order"
        self.root.preorder()

    def postorder(self):
        print 'Post-Order'
        self.root.postorder()

    def inorder(self):
        print 'In-Order'
        self.root.inorder()


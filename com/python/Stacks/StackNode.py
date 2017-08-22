class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.root
        self.root = newnode

    def pop(self):
        if Stack.isEmpty(self):
            return float('-inf')
        temp = self.root
        self.root = self.root.next
        return temp.data

    def peek(self):
        peek = self.root.data
        return peek

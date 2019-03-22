class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.min = []

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.min.append(data)
        else:
            if data <= self.min[0]:
                self.min.append(data)
            new_entry = Node(data)
            new_entry.next = self.head
            self.head = new_entry

    def pop(self):
        if self.head is None:
            raise Exception('pop called on an empty Stack')
        else:
            val = self.head.val
            self.head = self.head.next
            if val == self.min[0]:
                self.min = self.min[:-1]
            return val

    def getMin(self):
        if self.head is None:
            raise Exception('getMin called on an empty Stack')
        else:
            return self.min[-1]



import pdb

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            # pdb.set_trace()
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def print_list(self):
        if self.head is None:
            print("Empty List")
        else:
            curr = self.head
            res = []
            while curr is not None:
                res.append(curr.data)
                curr = curr.next
            print res

    def print_middle(self):
        if self.head is None  or self.head.next is None:
            return self.head
        fast = self.head
        slow = self.head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        print slow.data
        

    def nth_from_end(self, nth):
        if nth < 0:
            print "invalid entry"
        fast = self.head
        slow = self.head
        while nth is not 1:
            fast = fast.next
            nth = nth - 1
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        print slow.data

    def reverse_list(self):
        curr = self.head
        nextNode = self.head.next
        curr.next = None
        while nextNode:
            loop = nextNode.next
            nextNode.next = curr
            curr = nextNode
            nextNode = loop
        self.head = curr


    def removeDuplicates(self):
        if self.head is None:
            return self.head
        

    # def last_to_front(self):


    # def add_two_numbers_by_lists(self, first, second):
  

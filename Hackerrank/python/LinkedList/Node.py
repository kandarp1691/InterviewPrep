class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print current.data
            current = current.next

    def get_size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        return count

    def print_middle(self):
        pt1 = self.head
        pt2 = self.head

        while pt1 and pt1.next:
            pt2 = pt2.next
            pt1 = pt1.next.next

        print pt2.data

    def nth_from_end(self, nth):
        pt1 = self.head
        pt2 = self.head

        while nth-1 >= 0:
            pt1 = pt1.next
            nth = nth - 1

        while pt1:
            pt1 = pt1.next
            pt2 = pt2.next

        print pt2.data

    def reverse_list(self):
        current = self.head
        nextNode = self.head.next
        current.next = None
        while nextNode:
            loopNode = nextNode.next
            nextNode.next = current
            current = nextNode
            nextNode = loopNode
        self.head = current

    def removeDuplicates(self):
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def last_to_front(self):
        if self.head == None or self.head.next == None:
            return
        pt1 = self.head
        pt2 = self.head

        pt1 = pt1.next

        while pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next

        pt2.next = None
        pt1.next = self.head
        self.head = pt1

    def add_two_numbers_by_lists(self, first, second):
        temp = None
        prev = None
        carry = 0

        while first is not None or second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            sum = fdata + sdata + carry

            carry = 1 if sum >=10 else 0
            sum = sum if sum < 10 else sum%10

            temp = Node(sum)

            if self.head is None:
                temp = self.head
            else:
                prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp = Node(carry)

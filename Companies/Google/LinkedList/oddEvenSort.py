class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def oddEven(self,head):
        if head is None:
            return head
        current = head
        currnext = head.next

        while currnext.next is not None:
            if current.data % 2 == 0 and currnext.data % 2 == 1:
                return self.swap(current, currnext)
            elif current.data % 2 == 1:
                current = current.next
            elif currnext.data % 2 == 0:
                currnext = currnext.next


    def swap(self, node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp
        return node1




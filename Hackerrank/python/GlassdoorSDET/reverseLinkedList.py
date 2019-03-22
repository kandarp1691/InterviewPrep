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
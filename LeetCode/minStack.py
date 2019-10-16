# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxint
        self.minlist = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        minVal = self.min if not self.minlist else self.minlist[-1]
        if x <= minVal:
            self.minlist.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.getMin():
            self.minlist.pop(-1)
        self.stack = self.stack[:-1]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        print self.minlist
        return self.minlist[-1] if self.minlist else []

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print obj.top()
obj.pop()
print obj.getMin()
obj.pop()
print obj.getMin()
obj.pop()
obj.push(2147483647)
print obj.top()
print obj.getMin()
obj.push(-2147483648)
print obj.top()
print obj.getMin()
obj.pop()
print obj.getMin()


# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

#[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]
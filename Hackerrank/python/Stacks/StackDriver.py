# This is the driver program for implementation od Stack

from StackNode import *

stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)

while not stack.isEmpty():
    print stack.pop()
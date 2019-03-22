from StackNode import *


def next_greater_element(arr):
    stack = Stack()
    element = 0
    next = 0
    n = len(arr) - 1
    stack.push(arr[0])

    for i in range(1, n):
        next = arr[i]
        if not stack.isEmpty():
            element = stack.pop()

            while next > element:
                print str(element) + " --- " + str(next)
                if stack.isEmpty():
                    break
                element = stack.pop()

            if element > next:
                stack.push(element)

        stack.push(next)

    while not stack.isEmpty():
        element = stack.pop()
        next = -1
        print(str(element) + " --- " + str(next))

arr = [4,5,2,25]
next_greater_element(arr)

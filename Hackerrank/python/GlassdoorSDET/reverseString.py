def reverse(str):
    stack = []
    words = str.split()
    for i in words:
        stack.append(i)
    new_str = ''
    while len(stack) != 0:
        new_str = new_str+ stack.pop()
    print new_str
str = 'Hello world'
reverse(str)

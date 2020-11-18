def bracketnumber(string):
    left_num = 1
    stack = []
    for i in string:
        if i == '(':
            print left_num
            stack.append(left_num)
            left_num+=1
        if i == ')':
            print stack.pop()


bracketnumber('(a+(b*c))+(d/e)')


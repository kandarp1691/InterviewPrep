def morganAndString(a,b):
    stack_a = list(reversed(a))
    stack_b = list(reversed(b))
    res = []
    while len(stack_a) != 0 and len(stack_b) != 0:
        if ord(stack_a[-1]) > ord(stack_b[-1]):
            res.append(stack_b.pop())
        elif ord(stack_a[-1]) < ord(stack_b[-1]):
            res.append(stack_a.pop())
        else:
            stack_a_extras = []
            stack_b_extras = []
            i = len(stack_a)-1
            j = len(stack_b)-1
            while stack_a[i] == stack_b[j]:
                stack_a_extras.append(stack_a.pop())
                stack_b_extras.append(stack_b.pop())
                i = i-1
                j = j-1

            if ord(stack_a[-1]) > ord(stack_b[-1]):
                res.append(stack_b_extras.pop())
            elif ord(stack_a[-1]) < ord(stack_b[-1]):
                res.append(stack_a_extras.pop())
            while len(stack_a_extras) != 0 :
                stack_a.append(stack_a_extras.pop())
            while len(stack_b_extras) != 0 :
                stack_b.append(stack_b_extras.pop())

    while len(stack_a) != 0:
        res.append(stack_a.pop())

    while len(stack_b) != 0:
        res.append(stack_b.pop())

    return ''.join(res)

print morganAndString('JACK', 'DANIEL')


def evaluateExpression(expression):

    stack = []
    for val in expression.split(" "):
        if val in ['+', '-', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '+':
                result = op2 + op1
            if val == '-':
                result = op2 - op1
            if val == '*':
                result = op2 * op1
            if val == '/':
                result = op2/op1
            stack.append(result)
        else:
            stack.append(float(val))
    return stack.pop()

expression = '10 3 5 + *'
print evaluateExpression(expression)

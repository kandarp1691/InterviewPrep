def bracketChecker(arr):
    stack = []
    i = 0
    while i != len(arr):
        while arr[i] in '{[(':
            stack.append(arr[i])
            i = i+1
        if arr[i] == ')' and stack[-1] == '(':
            stack.pop()
            i = i+1
        elif arr[i] == '}' and stack[-1] == '{':
            stack.pop()
            i = i+1
        elif arr[i] == ']' and stack[-1] == '[':
            stack.pop()
            i = i+1
        else:
            return 'NO'
    return 'YES'

print bracketChecker('{(([])[])[]}[]')

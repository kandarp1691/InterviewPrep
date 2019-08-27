def isValid(string):
    stack = []
    valid = {"}":"{", ")":"(", "]":"["}
    for each in string:
        if each in valid:
            val = stack.pop()
            if valid[each] != val:
                return False
        else:
            stack.append(each)
    return not stack

print isValid('[]')
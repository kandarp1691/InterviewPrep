def isselfDivindNumbers(number):

    s = str(number)
    for i in s:
        if s%int(i)!= 0 or i == "0":
            return False
    return True

def selfDivingNumbers(left, right):
    result = []
    while left <= right:
        if isselfDivindNumbers(left):
            result.append(left)
        left = +1
    print result

selfDivingNumbers(1,22)



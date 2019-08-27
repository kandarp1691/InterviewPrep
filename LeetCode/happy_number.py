def isHappy(num):
    sum_list = []
    found = False
    while not found:
        s = 0
        for i in str(num):
            s = s+int(i)*int(i)
        if s == 1:
            found = True
        else:
            num = s
            if num in sum_list:
                break
            else:
                sum_list.append(num)
    return found

print isHappy(114)


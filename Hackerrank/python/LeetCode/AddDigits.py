def addDigits(num):
    num = str(num)
    sum = 0
    while len(str(num)) != 0:
        for i in str(num):
            sum = sum+int(i)
        num = sum

    print sum

addDigits(38)
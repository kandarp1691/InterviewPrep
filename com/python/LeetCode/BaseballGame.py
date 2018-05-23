def calPoints(ops):
    sum = 0
    valid_arr = []

    for i in range(0, len(ops)):
        if ops[i] == 'C':
            sum = sum-int(ops[i-1])
            valid_arr.remove((ops[i-1]))
        if ops[i] == 'D':
            valid_arr.append(2*sum)
            sum = sum + 2*sum
        if ops[i] == '+':
            val = valid_arr[0] + valid_arr[1]
            sum = sum + val
        else:
            sum = sum + int(ops[i])
    print sum

ops = ["5", "2", "C", "D", "+"]
calPoints(ops)
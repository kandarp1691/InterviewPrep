def count_max_consecutive_ones(str):
    count = 0
    res = 0
    for i in range(0, len(str)):
        if str[i] == 0:
            count = 0
        else:
            count = count+1
            res = max(res, count)
    return res

str = [1,1,1,0,0,0,0,0,1,1,1,1,1]
print count_max_consecutive_ones(str)
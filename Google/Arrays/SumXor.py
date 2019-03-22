def sumXor(n):
    count = 0
    for i in xrange(n):
        if i ^ n == i + n:
            count = count+1
    return count

print sumXor(100)
def getMoneySpent(keyboards, drives, s):
    # Complete this function
    total = s
    max = -1
    for i in range(0,len(keyboards)):
        for j in range(0, len(drives)):
            sum = keyboards[i] + drives[j]
            if sum > total:
                return max
            if sum > max and sum <= total:
                max = sum
    return max

keyboards = [4]
drives = [5]
s = 5
print getMoneySpent(keyboards, drives, s)


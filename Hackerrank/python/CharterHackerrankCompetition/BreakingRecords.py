#Find the time highest record is broken
def getRecords(arr):
    n = len(arr)
    highCount = 0
    lowCount = 0
    highest = arr[0]
    lowest = arr[0]
    for i in range(1, n):
        if arr[i] > highest:
            highest = arr[i]
            highCount += 1

    for i in range(1, n):
        if arr[i] < lowest:
            lowest = arr[i]
            lowCount += 1

    return highCount,lowCount

arr = [10,5,20,20,4,5,2,25,1]
print getRecords(arr)




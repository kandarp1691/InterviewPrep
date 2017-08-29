def birthdayCandles(arr):
    max = arr[0]
    count = 0
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] == max:
            count = count + 1
        else:
            count = 0

    return count

arr = [3,2,1,3,3,2,2,4,4,4,4,4,4,4]
print birthdayCandles(arr)
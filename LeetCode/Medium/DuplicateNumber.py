def dupNum(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            return arr[i]
print dupNum([1,3,4,2,2])
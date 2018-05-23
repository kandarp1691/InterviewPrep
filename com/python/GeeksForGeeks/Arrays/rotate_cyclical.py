# Cyclically rotate Array one by one
def rotate_cyclical(arr):
    n = len(arr)
    temp = arr[n-1]
    while n > 0:
        arr[n-1] = arr[n-2]
        n = n - 1
    arr[0] = temp
    return arr

print rotate_cyclical([1,2,3,4,5])